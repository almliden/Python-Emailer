# Python Email Adapter

## Example Usage

config = EmailAdapterConfigurator()
email_adapter = EmailAdapter(config.Config())

email_adapter.sendEmail(
  sender = 'from@example.com',
  receiver = 'to@example.com',
  subject = 'Example',
  message = '<h1>Message</h1>',
  content_type={ 'MIME-Version': '1.0' },
  sender_name='Sent email'
)