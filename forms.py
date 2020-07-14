from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class configForm(FlaskForm):
    sensorPiInterface = SelectField('Interface', choices=[('wlan0', 'wlan0'), ('wlan1', 'wlan1')])
    sensorPiChannels = StringField('Channels')
    mqttServer = StringField('MQTT Server')
    mqttPort = StringField('MQTT Server Port')
    splunkServer = StringField('Splunk Server')
    splunkPort = StringField('Splunk Server Port')
    splunkToken = StringField('Splunk Token')
    submit = SubmitField('Submit')