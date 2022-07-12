import os
import yagmail

def create_mail(event):
	return  {
		"subject": "Cepheus Registration Confirmation for {} and Further Steps".format(event.name),
		"body": f"""\
<h3>Greetings from Team Cepheus!</h3>
Hope you are doing well.
Thank you for registering for the <b>{event.name}</b>. Team Cepheus is excited to have you on board and we hope that you have a fun and fulfilling experience throughout the fest. <br>
<b>{event.description}</b>

<b>Please join our <a href='https://discord.gg/WP7zk2AgbK' target='_blank' rel='noreferrer'>Discord Server</a> to stay updated and ask any doubts.</b>
For regular updates, also check out our social media handles.
<a href='https://instagram.com/cepheus_iitgoa' target='_blank' rel='noreferrer'>Instagram</a>
<a href='https://twitter.com/cepheus_iitgoa' target='_blank' rel='noreferrer'>Twitter</a>
<a href='https://www.linkedin.com/in/cepheus-iit-goa/' target='_blank' rel='noreferrer'>LinkedIn</a>

For any queries, please go through the rulebook on our website: <a href='http://iitgoa.ac.in/cepheus' target='_blank' rel='noreferrer'>Cepheus 2022</a>
In case they're still not cleared, feel free to contact:
{event.manager_name}, Management Head: {event.manager_phone}
{event.head_name}, Event Head: {event.head_phone}

Buy Cepheus 2022 Official Merchandise at: <a href='https://cepheusmemories.co.in/' target='_blank' rel='noreferrer'>Cepheus Merchandise</a>
<img style="width:300px" src="https://i.imgur.com/uR6hRIx.png">


Best of luck!
Warm Regards
Team Cepheus
Indian Institute of Technology Goa

<img style="width:100%" src="https://i.imgur.com/9Il19un.png">
"""
	}

def send_registration_mail(user, event):
	mail = create_mail(event)
	yag = yagmail.SMTP(os.environ.get("MAILER_ID"), os.environ.get("MAILER_PASSWORD"))
	yag.send(to=user.email_id, subject=mail["subject"], contents=mail["body"])