{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eea47a70",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "complains={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a97189a1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===============================\n",
      "Your complaint has been received\n",
      "Welcome to Feedback_account\n",
      "Enter your name:jacinta\n",
      "Please choose your complain: issue\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'complains' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-8421d7c6d079>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Your complaint has been received'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[0mSubmit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-3-8421d7c6d079>\u001b[0m in \u001b[0;36mSubmit\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter your name:\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mcomplain\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Please choose your complain: \"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[1;32mfor\u001b[0m \u001b[0mcomplaints\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mcomplains\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeys\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcomplaints\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'==============================='\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'complains' is not defined"
     ]
    }
   ],
   "source": [
    "def Submit():\n",
    "    print(\"Welcome to Feedback_account\")\n",
    "    name = input(\"Enter your name:\")\n",
    "    complains = input(\"Please choose or enter your complains: \")\n",
    "    if(list(complains.keys())[-1]  == name and list(complaints.value())[-1] ==complains):\n",
    "    for complaints in complains.values()\n",
    "      print(complaints)\n",
    "    \n",
    "print('===============================')\n",
    "print('Your complaint has been received')\n",
    "   \n",
    "Submit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "871d5002",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "EOL while scanning string literal (<ipython-input-4-b588eaeadcbd>, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-b588eaeadcbd>\"\u001b[1;36m, line \u001b[1;32m11\u001b[0m\n\u001b[1;33m    'x-rapidapi-key': \"ed759af848msh3f1b3449dc5word= pick.split(' ')\u001b[0m\n\u001b[1;37m                                                                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m EOL while scanning string literal\n"
     ]
    }
   ],
   "source": [
    "def translate(choose, target):\n",
    "    import http.client\n",
    "\n",
    "conn = http.client.HTTPSConnection(\"google-translate1.p.rapidapi.com\")\n",
    "\n",
    "payload = \"q=Hello%2C%20world!&target=es&source=en\"\n",
    "\n",
    "headers = {\n",
    "    'content-type': \"application/x-www-form-urlencoded\",\n",
    "    'accept-encoding': \"application/gzip\",\n",
    "    'x-rapidapi-key': \"0f5d81958dmshfcc048b3c986295p1a5280jsn7a1beabd6131\",\n",
    "    'x-rapidapi-host': \"google-translate1.p.rapidapi.com\"\n",
    "    }\n",
    "\n",
    "conn.request(\"POST\", \"/language/translate/v2\", payload, headers)\n",
    "\n",
    "res = conn.getresponse()\n",
    "data = res.read()\n",
    "\n",
    "print(data.decode(\"utf-8\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3556a2ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "def detect(choose):\n",
    "    url = \"https://google-translate1.p.rapidapi.com/language/translate/v2/detect\"\n",
    "    \n",
    "    word= pick.split(' ')\n",
    "    payload= f\"q={'%20'.join(word)}\"\n",
    "    headers = {\n",
    "    'content-type': \"application/x-www-form-urlencoded\",\n",
    "    'accept-encoding': \"application/gzip\",\n",
    "    'x-rapidapi-key': \"ed759af848msh3f1b3449dc5a814p19dc1cjsn744f99072628\",\n",
    "    'x-rapidapi-host': \"google-translate1.p.rapidapi.com\"\n",
    "    }\n",
    "\n",
    "    response = requests.request(\"POST\", url, data=payload, headers=headers)\n",
    "    print(response.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f828600",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
