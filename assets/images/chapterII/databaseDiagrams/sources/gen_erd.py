#!/usr/bin/env python3
"""Genera el Physical Schema ERD de Guardian+ y los zoom por bounded context."""
import subprocess, sys, os

# (columna, tipo, marca)  marca: PK | FK | UQ | FK/UQ | ''
SCHEMA = {
 "IAM": {
  "user_accounts": [("id","UUID","PK"),("email","VARCHAR(255)","UQ"),("password_hash","VARCHAR(255)",""),
    ("email_verified","BOOLEAN",""),("two_factor_enabled","BOOLEAN",""),("status","VARCHAR(30)",""),
    ("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "otp_codes": [("id","UUID","PK"),("user_id","UUID","FK"),("code_hash","VARCHAR(255)",""),
    ("purpose","VARCHAR(30)",""),("expires_at","TIMESTAMP",""),("used_at","TIMESTAMP",""),("created_at","TIMESTAMP","")],
  "password_reset_tokens": [("id","UUID","PK"),("user_id","UUID","FK"),("token_hash","VARCHAR(255)",""),
    ("expires_at","TIMESTAMP",""),("used_at","TIMESTAMP",""),("created_at","TIMESTAMP","")],
 },
 "PROFILE": {
  "user_profiles": [("id","UUID","PK"),("user_id","UUID","FK"),("first_name","VARCHAR(100)",""),
    ("last_name","VARCHAR(100)",""),("phone_number","VARCHAR(30)",""),("profile_image_url","TEXT",""),
    ("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "care_recipient_profiles": [("id","UUID","PK"),("created_by_user_id","UUID","FK"),("first_name","VARCHAR(100)",""),
    ("last_name","VARCHAR(100)",""),("birth_date","DATE",""),("profile_image_url","TEXT",""),
    ("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "care_relationships": [("id","UUID","PK"),("user_id","UUID","FK"),("care_recipient_profile_id","UUID","FK"),
    ("relationship_type","VARCHAR(30)",""),("status","VARCHAR(30)",""),("started_at","TIMESTAMP",""),("ended_at","TIMESTAMP","")],
  "user_preferences": [("id","UUID","PK"),("user_id","UUID","FK/UQ"),("language","VARCHAR(20)",""),
    ("notifications_enabled","BOOLEAN",""),("high_contrast_enabled","BOOLEAN",""),
    ("voice_assistance_enabled","BOOLEAN",""),("font_scale","DECIMAL(3,2)",""),("updated_at","TIMESTAMP","")],
 },
 "SUBSCRIPTIONS": {
  "subscription_plans": [("id","UUID","PK"),("name","VARCHAR(100)","UQ"),("description","TEXT",""),
    ("price","DECIMAL(10,2)",""),("currency","VARCHAR(10)",""),("billing_cycle","VARCHAR(30)",""),
    ("active","BOOLEAN",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "subscriptions": [("id","UUID","PK"),("subscriber_user_id","UUID","FK"),("plan_id","UUID","FK"),
    ("status","VARCHAR(30)",""),("current_period_start","TIMESTAMP",""),("current_period_end","TIMESTAMP",""),
    ("cancel_at_period_end","BOOLEAN",""),("cancelled_at","TIMESTAMP",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "payments": [("id","UUID","PK"),("subscription_id","UUID","FK"),("payment_type","VARCHAR(30)",""),
    ("amount","DECIMAL(10,2)",""),("currency","VARCHAR(10)",""),("provider","VARCHAR(50)",""),
    ("provider_reference","VARCHAR(255)",""),("status","VARCHAR(30)",""),("paid_at","TIMESTAMP",""),("created_at","TIMESTAMP","")],
  "entitlements": [("id","UUID","PK"),("code","VARCHAR(80)","UQ"),("name","VARCHAR(100)",""),("description","TEXT","")],
  "plan_entitlements": [("id","UUID","PK"),("plan_id","UUID","FK"),("entitlement_id","UUID","FK")],
  "subscription_entitlements": [("id","UUID","PK"),("subscription_id","UUID","FK"),("entitlement_id","UUID","FK"),
    ("status","VARCHAR(30)",""),("effective_from","TIMESTAMP",""),("effective_to","TIMESTAMP","")],
 },
 "HEALTH MONITORING": {
  "wearable_devices": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK"),("serial_number","VARCHAR(100)","UQ"),
    ("device_type","VARCHAR(50)",""),("status","VARCHAR(30)",""),("assigned_at","TIMESTAMP",""),
    ("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "vital_sign_types": [("id","UUID","PK"),("code","VARCHAR(50)","UQ"),("name","VARCHAR(100)",""),("unit","VARCHAR(30)","")],
  "vital_sign_readings": [("id","UUID","PK"),("wearable_device_id","UUID","FK"),("care_recipient_profile_id","UUID","FK"),
    ("vital_sign_type_id","UUID","FK"),("value","DECIMAL(10,2)",""),("measured_at","TIMESTAMP",""),("received_at","TIMESTAMP","")],
  "vital_sign_thresholds": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK"),("vital_sign_type_id","UUID","FK"),
    ("minimum_value","DECIMAL(10,2)",""),("maximum_value","DECIMAL(10,2)",""),("required_consecutive_hits","INT",""),
    ("active","BOOLEAN",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "health_reports": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK"),("generated_by_user_id","UUID","FK"),
    ("report_type","VARCHAR(30)",""),("period_start","DATE",""),("period_end","DATE",""),("summary","TEXT",""),("generated_at","TIMESTAMP","")],
 },
 "EMERGENCY &amp; ALERTING": {
  "alerts": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK"),("source_type","VARCHAR(40)",""),
    ("source_reference_id","UUID",""),("severity","VARCHAR(30)",""),("status","VARCHAR(30)",""),
    ("triggered_at","TIMESTAMP",""),("acknowledged_at","TIMESTAMP",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "alert_deliveries": [("id","UUID","PK"),("alert_id","UUID","FK"),("recipient_user_id","UUID","FK"),
    ("recipient_level","VARCHAR(30)",""),("channel","VARCHAR(30)",""),("delivery_status","VARCHAR(30)",""),
    ("sent_at","TIMESTAMP",""),("delivered_at","TIMESTAMP","")],
  "alert_responses": [("id","UUID","PK"),("alert_id","UUID","FK"),("responder_user_id","UUID","FK"),
    ("response_status","VARCHAR(30)",""),("claimed_at","TIMESTAMP",""),("completed_at","TIMESTAMP",""),("notes","TEXT","")],
  "incidents": [("id","UUID","PK"),("alert_id","UUID","FK/UQ"),("status","VARCHAR(30)",""),
    ("marked_in_attention_at","TIMESTAMP",""),("stabilized_at","TIMESTAMP",""),("closed_at","TIMESTAMP",""),
    ("notes","TEXT",""),("created_at","TIMESTAMP","")],
  "alert_settings": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK/UQ"),("primary_ack_timeout_sec","INT",""),
    ("escalation_enabled","BOOLEAN",""),("silent_mode_enabled","BOOLEAN",""),("updated_at","TIMESTAMP","")],
  "emergency_contacts": [("id","UUID","PK"),("care_recipient_profile_id","UUID","FK"),("user_id","UUID","FK"),
    ("priority_order","INT",""),("active","BOOLEAN",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "alert_channel_settings": [("id","UUID","PK"),("user_id","UUID","FK"),("channel","VARCHAR(30)",""),
    ("enabled","BOOLEAN",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
 },
 "CARE ROUTINES &amp; WELLNESS": {
  "reminders": [("id","UUID","PK"),("person_under_care_id","UUID","FK"),("type","VARCHAR(30)",""),
    ("scheduled_time","TIMESTAMP",""),("issued_at","TIMESTAMP",""),("status","VARCHAR(30)",""),
    ("reissue_count","INT",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "sleep_cycle_records": [("id","UUID","PK"),("person_under_care_id","UUID","FK"),("wearable_device_id","UUID","FK"),
    ("start_time","TIMESTAMP",""),("end_time","TIMESTAMP",""),("interruption_count","INT",""),("classification","VARCHAR(30)","")],
  "activity_monitors": [("id","UUID","PK"),("person_under_care_id","UUID","FK/UQ"),("wearable_device_id","UUID","FK"),
    ("status","VARCHAR(30)",""),("inactivity_since","TIMESTAMP","")],
  "medication_stocks": [("id","UUID","PK"),("person_under_care_id","UUID","FK/UQ"),("remaining_doses","INT",""),
    ("daily_consumption","DECIMAL(5,2)",""),("last_acquisition_date","TIMESTAMP","")],
 },
 "MOBILITY &amp; GEOFENCING": {
  "safe_zones": [("id","UUID","PK"),("fragile_citizen_id","UUID","FK"),("name","VARCHAR(100)",""),
    ("latitude","DECIMAL(9,6)",""),("longitude","DECIMAL(9,6)",""),("radius_in_meters","DECIMAL(10,2)",""),
    ("status","VARCHAR(30)",""),("created_at","TIMESTAMP",""),("updated_at","TIMESTAMP","")],
  "location_trackings": [("id","UUID","PK"),("fragile_citizen_id","UUID","FK/UQ"),("current_latitude","DECIMAL(9,6)",""),
    ("current_longitude","DECIMAL(9,6)",""),("accuracy_in_meters","DECIMAL(6,2)",""),
    ("current_status","VARCHAR(30)",""),("last_updated_at","TIMESTAMP","")],
  "location_records": [("id","UUID","PK"),("location_tracking_id","UUID","FK"),("wearable_device_id","UUID","FK"),
    ("latitude","DECIMAL(9,6)",""),("longitude","DECIMAL(9,6)",""),("accuracy_in_meters","DECIMAL(6,2)",""),
    ("status","VARCHAR(30)",""),("recorded_at","TIMESTAMP","")],
  "zone_violations": [("id","UUID","PK"),("safe_zone_id","UUID","FK"),("fragile_citizen_id","UUID","FK"),
    ("latitude","DECIMAL(9,6)",""),("longitude","DECIMAL(9,6)",""),("detected_at","TIMESTAMP","")],
 },
}

# (tabla_padre, tabla_hija, cardinalidad_hija)
RELS = [
 ("user_accounts","otp_codes","N"),
 ("user_accounts","password_reset_tokens","N"),
 ("user_accounts","user_profiles","0..1"),
 ("user_accounts","user_preferences","0..1"),
 ("user_accounts","care_recipient_profiles","N"),
 ("user_accounts","care_relationships","N"),
 ("care_recipient_profiles","care_relationships","N"),
 ("user_accounts","subscriptions","N"),
 ("subscription_plans","subscriptions","N"),
 ("subscriptions","payments","N"),
 ("subscription_plans","plan_entitlements","N"),
 ("entitlements","plan_entitlements","N"),
 ("subscriptions","subscription_entitlements","N"),
 ("entitlements","subscription_entitlements","N"),
 ("care_recipient_profiles","wearable_devices","N"),
 ("wearable_devices","vital_sign_readings","N"),
 ("care_recipient_profiles","vital_sign_readings","N"),
 ("vital_sign_types","vital_sign_readings","N"),
 ("care_recipient_profiles","vital_sign_thresholds","N"),
 ("vital_sign_types","vital_sign_thresholds","N"),
 ("care_recipient_profiles","health_reports","N"),
 ("user_accounts","health_reports","N"),
 ("care_recipient_profiles","alerts","N"),
 ("alerts","alert_deliveries","N"),
 ("user_accounts","alert_deliveries","N"),
 ("alerts","alert_responses","N"),
 ("user_accounts","alert_responses","N"),
 ("alerts","incidents","0..1"),
 ("care_recipient_profiles","alert_settings","0..1"),
 ("care_recipient_profiles","emergency_contacts","N"),
 ("user_accounts","emergency_contacts","N"),
 ("user_accounts","alert_channel_settings","N"),
 ("care_recipient_profiles","reminders","N"),
 ("care_recipient_profiles","sleep_cycle_records","N"),
 ("wearable_devices","sleep_cycle_records","N"),
 ("care_recipient_profiles","activity_monitors","0..1"),
 ("wearable_devices","activity_monitors","N"),
 ("care_recipient_profiles","medication_stocks","0..1"),
 ("care_recipient_profiles","safe_zones","N"),
 ("care_recipient_profiles","location_trackings","0..1"),
 ("location_trackings","location_records","N"),
 ("wearable_devices","location_records","N"),
 ("safe_zones","zone_violations","N"),
 ("care_recipient_profiles","zone_violations","N"),
]

HDR = "#d9d9f5"
HDR_EXT = "#e6e6e6"

def table_node(name, cols, external=False):
    hdr = HDR_EXT if external else HDR
    rows = ['<TR><TD COLSPAN="3" BGCOLOR="%s" ALIGN="LEFT"><B>%s</B></TD></TR>' % (hdr, name)]
    for col, typ, mark in cols:
        rows.append(
          '<TR><TD ALIGN="RIGHT"><FONT POINT-SIZE="8">%s</FONT></TD>'
          '<TD ALIGN="LEFT">%s</TD><TD ALIGN="LEFT">%s</TD></TR>' % (mark or " ", col, typ))
    return '  "%s" [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="3">%s</TABLE>>];' % (
        name, "".join(rows))

def build(path, contexts, include_external=True, rankdir="TB", title=None):
    tables = {t: c for ctx in contexts for t, c in SCHEMA[ctx].items()}
    ext = {}
    if include_external:
        for ctx, ts in SCHEMA.items():
            if ctx in contexts: continue
            for t, c in ts.items():
                if any((p == t and h in tables) or (h == t and p in tables) for p, h, _ in RELS):
                    ext[t] = c
    out = ["digraph ERD {", '  graph [rankdir=%s, splines=ortho, nodesep=0.45, ranksep=0.9, fontname="Helvetica", bgcolor="white"];' % rankdir,
           '  node [shape=plaintext, fontname="Helvetica", fontsize=11];',
           '  edge [fontname="Helvetica", fontsize=9, color="#555555", arrowhead=crow, arrowtail=tee, dir=both];']
    if title:
        out.append('  labelloc="t"; fontsize=22; label="%s";' % title)
    for i, ctx in enumerate(contexts):
        out.append('  subgraph cluster_%d {' % i)
        out.append('    label="%s"; fontsize=18; color="#bbbbbb"; style="rounded"; margin=18;' % ctx)
        for t, c in SCHEMA[ctx].items():
            out.append("  " + table_node(t, c))
        out.append("  }")
    if ext:
        out.append('  subgraph cluster_ext {')
        out.append('    label="Referencias externas"; fontsize=14; color="#dddddd"; style="dashed"; margin=14;')
        for t, c in ext.items():
            out.append("  " + table_node(t, c, external=True))
        out.append("  }")
    known = set(tables) | set(ext)
    for parent, child, card in RELS:
        if parent in known and child in known:
            out.append('  "%s" -> "%s" [headlabel="%s", taillabel="1"];' % (parent, child, card))
    out.append("}")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")

def render(dot_path, png_path, engine="dot"):
    subprocess.run([engine, "-Tpng", "-Gdpi=110", dot_path, "-o", png_path], check=True)

if __name__ == "__main__":
    base = sys.argv[1]
    jobs = [
      ("erd-global.dot", "erd-global.png", list(SCHEMA.keys()), False, "TB",
       "Guardian+ — Physical Schema ERD", "fdp", "polyline"),
      ("care-routines-db.dot", "care-routines-db.png", ["CARE ROUTINES &amp; WELLNESS"], True, "LR", None, "dot", "ortho"),
      ("mobility-db.dot", "mobility-db.png", ["MOBILITY &amp; GEOFENCING"], True, "LR", None, "dot", "ortho"),
    ]
    for dot, png, ctxs, ext, rankdir, title, engine, splines in jobs:
        dp, pp = os.path.join(base, dot), os.path.join(base, png)
        build(dp, ctxs, ext, rankdir, title)
        if splines != "ortho":
            src = open(dp, encoding="utf-8").read().replace("splines=ortho", "splines=" + splines)
            open(dp, "w", encoding="utf-8").write(src)
        render(dp, pp, engine)
        print("ok", png, engine)
