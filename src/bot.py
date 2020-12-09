import requests 


def send_message(message:str, hook_url)->None:
    """sends message to link

    Args:
        data (str): the message you want to send
    """

    msg = {
      "content": message
    }

    requests.post(hook_url, data = msg) # bot post


    