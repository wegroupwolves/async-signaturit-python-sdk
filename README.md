Signaturit Python SDK
=====================
This package is a wrapper for Signaturit Api. If you didn't read the documentation yet, maybe it's time to take a look [here](http://docs.signaturit.com/).

You can install the package through pip.

```bash
sudo pip install signaturit_sdk
```

Configuration
-------------
Just import the Signaturit Client this way

```python
from signaturit_sdk.signaturit_client import SignaturitClient
```

Then you can authenticate yourself using your AuthToken

```python
client = SignaturitClient('TOKEN')
```

Remember, the default calls are made to our Sandbox server. If you want to do in production, just set the flag when you do the call.

```python
client = SignaturitClient('TOKEN', SignaturitClient.PRODUCTION)
```

Examples
--------

## Signature request

### Get all signature requests

Retrieve all data from your signature requests using different filters.

##### All signatures

```python
response = client.get_signatures()
```

##### Getting the last 50 signatures

```python
response = client.get_signatures(limit=50)
```

##### Getting the following last 50 signatures

```python
response = client.get_signatures(limit=50, offset=50)
```

##### Getting only the finished signatures 

```python
response = client.get_signatures(conditions={'status': 3})
```

##### Getting the finished signatures created since July 20th of 2014

```python
response = client.get_signatures(conditions={'since': '2014-7-20', 'status': 3})
```

##### Getting signatures with custom field "crm_id"

```python
response = client.get_signatures(conditions={'data': {'crm_id': 'CUSTOM_ID'}})
```
##### Getting signatures inside a set of ids

```python
response = client.get_signatures(conditions={'ids': ['ID1', 'ID2]})
``

### Count signature requests

Count your signature requests.

```python
response = client.count_signatures()
```

### Get signature request

Get a single signature request.

```python
response = client.get_signature('SIGNATURE_ID')
```

### Get signature documents

Get all documents from a signature request.

```python
response = client.get_signature_documents('SIGNATURE_ID')
```

### Get signature document

Get a single document from a signature request.

```python
response = client.get_signature_document('SIGNATURE_ID','DOCUMENT_ID')
```

### Signature request

Create a new signature request. Check all [params](http://docs.signaturit.com/api/#sign_create_sign).

```python
recipients =  [{'fullname': 'Bob', 'email': 'bobsoap@signatur.it'}]
sign_params = {'subject': 'Receipt number 250', 'body': 'Please, can you sign this document?'}
file_path = '/documents/contracts/125932_important.pdf'
response = client.create_signature(file_path, recipients, sign_params)
```

You can enable the security mode, by setting the recipient phone.

```python
recipients =  [{'fullname': 'Bob', 'email': 'bobsoap@signatur.it', 'phone': 'XXXXX}]'}]
```

Then, the user will receive a SMS in the phone number with a security code, needed to begin the sign process.

And if you have some templates created, you can use them too.

```python
recipients =  [{'fullname': 'Bob', 'email': 'bobsoap@signatur.it'}]
sign_params = {'subject': 'Receipt number 250', 'body': 'Please, can you sign this document?', 'templates': ['id1',...]}
file_path = []
response = client.create_signature(file_path, recipients, sign_params)
```


You can send templates with the fields filled

```python
recipients =  [{'fullname': 'Bob', 'email': 'bobsoap@signatur.it'}]
sign_params = {'subject': 'Receipt number 250', 'body': 'Please, can you sign this document?', 'templates': {'TEMPLATE_ID'}, 'data': {'WIDGET_ID': 'DEFAULT_VALUE'}}

response = client.create_signature({}, recipients, sign_params)
```

You can add custom info in your requests

```python
recipients =  [{'fullname': 'Bob', 'email': 'bobsoap@signatur.it'}]
sign_params = {'subject': 'Receipt number 250', 'body': 'Please, can you sign this document?', 'data': {'crm_id': '45673'}}
file_path = '/documents/contracts/125932_important.pdf'
response = client.create_signature(file_path, recipients, sign_params)
```

### Cancel signature request

Cancel a signature request.

```python
response = client.cancel_signature('SIGNATURE_ID');
```

### Send reminder

Send a reminder email.

```python
response = client.send_signature_reminder('SIGNATURE_ID', 'DOCUMENT_ID');
```

### Get audit trail

Get the audit trail of a signature request document and save it in the submitted path.

```python
response = client.download_audit_trail('ID','DOCUMENT_ID','/path/doc.pdf')
```

### Get signed document

Get the signed document of a signature request document and save it in the submitted path.

```python
response = client.download_signed_document('ID','DOCUMENT_ID','/path/doc.pdf')
```

## Account

### Get account

Retrieve the information of your account.

```python
response = client.get_account()
```

## Branding

### Get brandings

Get all account brandings.

```python
response = client.get_brandings()
```

### Get branding

Get a single branding.

```python
response = client.get_branding('BRANDING_ID')
```

### Create branding

Create a new branding. You can check all branding params [here](http://docs.signaturit.com/api/#set_branding).`

```python
branding_params = {'corporate_layout_color': '#FFBF00',
                   'corporate_text_color': '#2A1B0A',
                   'application_texts': {'sign_button': 'Sign!'}
}
response = client.create_branding(branding_params)
```

### Update branding

Update a single branding.

```python
branding_params = {'application_texts': {'send_button': 'Send!'}}
response = client.update_branding('BRANDING_ID', branding_params)
```

### Update branding logo

Change the branding logo.

```python
file_path = '/path/new_logo.png'
response = client.update_branding_logo('BRANDING_ID', file_path)
```

### Update branding template

Change a template. Learn more about the templates [here](http://docs.signaturit.com/api/#put_template_branding).

```python
file_path = '/path/new_template.html'
response = client.update_branding_email('BRANDING_ID', 'sign_request', file_path)
```

##Templates

### Get templates

Retrieve all data from your templates.

```python
response = client.get_templates()
```

##Emails

### Get emails

####Get all certified emails

```python
response = client.get_emails()
```

####Get last 50 emails

```python
response = client.get_emails(50)
```

####Navigate through all emails in blocks of 50 results

```python
response = client.get_emails(50, 50)
```

### Count emails

Count all certified emails

```python
response = client.count_emails()
```

### Get email

Get a single email

```python
client.get_email('EMAIL_ID')
```

### Get email certificates

Get a single email certificates

```python
client.get_email_certificates('EMAIL_ID')
```

### Get email certificate

Get a single email certificate

```python
client.get_email('EMAIL_ID', 'CERTIFICATE_ID')
```

### Create email

Create a new certified emails.

```python
response = client.create_email(
    [ 'demo.pdf', 'receip.pdf' ],
    [{'email': 'john.doe@signaturit.com', 'fullname': 'Mr John'}],
    'Python subject',
    'Python body',
    {}
)
```

### Get original document

Get the original document of an email request and save it in the submitted path.

```python
response = client.download_email_original_file('EMAIL_ID','CERTIFICATE_ID','/path/doc.pdf')
```

### Get audit trail document

Get the audit trail document of an email request and save it in the submitted path.

```python
response = client.download_email_audit_trail('EMAIL_ID','CERTIFICATE_ID','/path/doc.pdf')
```
