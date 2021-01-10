import configparser
import smtplib, ssl
import os

class EmailAdapterConfig:
  port = 465
  account = None
  password = None
  # domain = None
  server = None

class EmailAdapter:
  config = EmailAdapterConfig
  context = None

  def __init__(self, emailAdapterConfig=None):
    print(emailAdapterConfig)
    if (emailAdapterConfig != None):
      self.config = emailAdapterConfig

  def sendEmail(self, sender, receiver, subject, message, sender_text = None, content_type = None):
    self.context = ssl.create_default_context()
    with smtplib.SMTP_SSL(self.config.server, self.config.port, context=self.context) as server:
      server.login(self.config.account, self.config.password)
      message_text = ("""\
        From: %s
        To: %s
        Subject: %s 

        %s
        """ % (sender, receiver, subject, message))
      server.sendmail(sender, receiver, message_text)

class EmailAdapterConfigurator:
  config = None
  configName = None

  def __init__(self, EmailAdapterConfig=None):
    if (EmailAdapterConfig != None):
      self.config = EmailAdapterConfig
    self.configName = 'config.ini'

  def Config(self, fileName=None):
    if not os.path.isfile(self.configName):
      raise FileExistsError("Config file not found")
    parser=configparser.ConfigParser()
    parser.read(self.configName)
    self.config = EmailAdapterConfig
    self.config.port = int(parser.get('Email', 'EMAIL_PORT', fallback = 465))
    self.config.account = parser.get('Email', 'EMAIL_ACCOUNT', fallback = None)
    self.config.password = parser.get('Email', 'EMAIL_PASSWORD', fallback = None)
    # self.config.domain = parser.get('Email', 'EMAIL_DOMAIN', fallback = None)
    self.config.server = parser.get('Email', 'EMAIL_SERVER', fallback = None)
    return self.config

config = EmailAdapterConfigurator()
emailAdapter = EmailAdapter(config.Config())

