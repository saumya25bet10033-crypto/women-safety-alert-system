{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "24f2dcca-5348-4c50-82fd-48f41aec5ed7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The woman should run to the police station 150 meters away for quickest help.\n"
     ]
    }
   ],
   "source": [
    "# Distances of police stations from the woman (in meters)\n",
    "police_stations = [500, 200, 350, 150, 400]\n",
    "\n",
    "# Greedy choice: choose the minimum distance\n",
    "min_distance = police_stations[0]\n",
    "for d in police_stations:\n",
    "    if d < min_distance:\n",
    "        min_distance = d\n",
    "\n",
    "print(\"The woman should run to the police station\", min_distance, \"meters away for quickest help.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9fcd015a-03a5-4d09-8610-084ff8d64810",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shortest path: ['Woman', 'Shop', 'Road', 'Police']\n",
      "Total distance: 5\n",
      "Woman reached the police and informed them about the danger.\n"
     ]
    }
   ],
   "source": [
    "# Graph distances (cost)\n",
    "graph = {\n",
    "    'Woman': {'Shop': 2, 'Crowd': 3},\n",
    "    'Shop': {'Road': 2},\n",
    "    'Crowd': {'Park': 4},\n",
    "    'Road': {'Police': 1},\n",
    "    'Park': {'Police': 2},\n",
    "    'Police': {}\n",
    "}\n",
    "# Heuristic guess (straight-line distance to Police)\n",
    "h = {\n",
    "    'Woman': 4,\n",
    "    'Shop': 2,\n",
    "    'Crowd': 3,\n",
    "    'Road': 1,\n",
    "    'Park': 2,\n",
    "    'Police': 0\n",
    "}\n",
    "start = 'Woman'\n",
    "goal = 'Police'\n",
    "open_set = [start]\n",
    "g = {start: 0}\n",
    "came = {}\n",
    "while open_set:\n",
    "    # find node with smallest f = g + h\n",
    "    current = open_set[0]\n",
    "    for node in open_set:\n",
    "        if g.get(node, 999) + h[node] < g.get(current, 999) + h[current]:\n",
    "            current = node\n",
    "    if current == goal:\n",
    "        break\n",
    "    open_set.remove(current)\n",
    "    for neigh in graph[current]:\n",
    "        temp = g[current] + graph[current][neigh]\n",
    "        if temp < g.get(neigh, 999):\n",
    "            g[neigh] = temp\n",
    "            came[neigh] = current\n",
    "            if neigh not in open_set:\n",
    "                open_set.append(neigh)\n",
    "# path reconstruction\n",
    "path = [goal]\n",
    "while path[-1] != start:\n",
    "    path.append(came[path[-1]])\n",
    "path.reverse()\n",
    "print(\"Shortest path:\", path)\n",
    "print(\"Total distance:\", g[goal])\n",
    "print(\"Woman reached the police and informed them about the danger.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4e1a9b34-0959-4056-a7c3-41309945e96b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before exchange:\n",
      "Woman: Help Needed\n",
      "Police: On the Way\n",
      "\n",
      "After exchange:\n",
      "Woman received: On the Way\n",
      "Police received: Help Needed\n"
     ]
    }
   ],
   "source": [
    "# Woman wants to send a help alert to Police\n",
    "woman_message = \"Help Needed\"\n",
    "police_message = \"On the Way\"\n",
    "\n",
    "print(\"Before exchange:\")\n",
    "print(\"Woman:\", woman_message)\n",
    "print(\"Police:\", police_message)\n",
    "\n",
    "# Exchange (swap) the values\n",
    "temp = woman_message\n",
    "woman_message = police_message\n",
    "police_message = temp\n",
    "\n",
    "print(\"\\nAfter exchange:\")\n",
    "print(\"Woman received:\", woman_message)\n",
    "print(\"Police received:\", police_message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5c24a980-754d-4e12-bfab-521a4e9b0116",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Woman sent character code: 7\n",
      "Police converted it to number: 7\n",
      "Police: High alert! Heading to help the woman.\n"
     ]
    }
   ],
   "source": [
    "# Woman sends a secret character code to the police\n",
    "secret_char = '7'   # Woman's alert level as a character\n",
    "\n",
    "print(\"Woman sent character code:\", secret_char)\n",
    "\n",
    "# Base conversion: character to number\n",
    "# ord('0') = 48, ord('7') = 55 → 55 - 48 = 7\n",
    "alert_level = ord(secret_char) - ord('0')\n",
    "\n",
    "print(\"Police converted it to number:\", alert_level)\n",
    "\n",
    "# Police reacts based on number\n",
    "if alert_level > 5:\n",
    "    print(\"Police: High alert! Heading to help the woman.\")\n",
    "else:\n",
    "    print(\"Police: Low alert. Sending nearest patrol team.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "403711ac-f7ae-4f7e-942f-de6ff4258b44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Woman sent code: 4\n",
      "Converted alert level: 4\n",
      "Police: Moderate alert. Nearby patrol alerted.\n"
     ]
    }
   ],
   "source": [
    "# Woman sends a secret character alert code\n",
    "secret_char = '4'   # example character\n",
    "\n",
    "print(\"Woman sent code:\", secret_char)\n",
    "\n",
    "# Convert character to number\n",
    "alert = ord(secret_char) - ord('0')\n",
    "\n",
    "print(\"Converted alert level:\", alert)\n",
    "\n",
    "# IF – ELIF – ELSE conditions\n",
    "if alert >= 8:\n",
    "    print(\"Police: Extreme danger! Team dispatched immediately!\")\n",
    "elif alert >= 5:\n",
    "    print(\"Police: High alert! Moving towards the woman.\")\n",
    "elif alert >= 3:\n",
    "    print(\"Police: Moderate alert. Nearby patrol alerted.\")\n",
    "else:\n",
    "    print(\"Police: Low alert. Monitoring the situation.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "555e3f10-7a1a-4986-8f8b-9567ff4d4540",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Woman sends alert code (0-9):  \n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error: You must enter a number from 0 to 9.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Woman sends alert code (0-9):  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Converted alert level: 5\n",
      "Police: High alert! Police moving towards the woman.\n"
     ]
    }
   ],
   "source": [
    "# Woman keeps sending alert codes until police get a high alert\n",
    "\n",
    "while True:\n",
    "    secret_char = input(\"Woman sends alert code (0-9): \")\n",
    "\n",
    "    # Prevent empty input\n",
    "    if secret_char == \"\":\n",
    "        print(\"Error: You must enter a number from 0 to 9.\")\n",
    "        continue\n",
    "\n",
    "    # Take only the first character\n",
    "    secret_char = secret_char[0]\n",
    "\n",
    "    # If not a digit, show error\n",
    "    if not ('0' <= secret_char <= '9'):\n",
    "        print(\"Invalid input! Please enter digits only (0-9).\")\n",
    "        continue\n",
    "\n",
    "    # Character to number conversion\n",
    "    alert = ord(secret_char) - ord('0')\n",
    "    print(\"Converted alert level:\", alert)\n",
    "\n",
    "    # Conditions\n",
    "    if alert >= 8:\n",
    "        print(\"Police: Extreme danger! Rushing immediately!\")\n",
    "        break\n",
    "    elif alert >= 5:\n",
    "        print(\"Police: High alert! Police moving towards the woman.\")\n",
    "        break\n",
    "    elif alert >= 3:\n",
    "        print(\"Police: Moderate alert. Asking woman to stay calm.\")\n",
    "    else:\n",
    "        print(\"Police: Low alert. Monitoring… Woman can send again.\")\n",
    "\n",
    "    print()  # blank line for clarity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "28318bd6-7e67-4e3a-9577-c3adb005eb4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WOMAN SAFETY SYSTEM – GCD CALCULATOR\n",
      "Enter two positive numbers to calculate GCD.\n",
      "Enter 0 anytime to stop.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  5\n",
      "Enter second number:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GCD of 5 and 8 is: 1\n",
      "Police: Low Alert. Woman may continue sending values.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  6\n",
      "Enter second number:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GCD of 6 and 4 is: 2\n",
      "Police: Low Alert. Woman may continue sending values.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting system… Stay safe!\n"
     ]
    }
   ],
   "source": [
    "# Woman Safety Alert + GCD Finder\n",
    "print(\"WOMAN SAFETY SYSTEM – GCD CALCULATOR\")\n",
    "print(\"Enter two positive numbers to calculate GCD.\")\n",
    "print(\"Enter 0 anytime to stop.\\n\")\n",
    "while True:\n",
    "    a = input(\"Enter first number: \")\n",
    "    # Prevent empty input\n",
    "    if a == \"\":\n",
    "        print(\"Error: Input cannot be empty.\")\n",
    "        continue\n",
    "    # Convert to int safely\n",
    "    if not a.isdigit():\n",
    "        print(\"Please enter digits only.\")\n",
    "        continue\n",
    "    a = int(a)\n",
    "    if a == 0:\n",
    "        print(\"Exiting system… Stay safe!\")\n",
    "        break\n",
    "    b = input(\"Enter second number: \")\n",
    "    if b == \"\":\n",
    "        print(\"Error: Input cannot be empty.\")\n",
    "        continue\n",
    "    if not b.isdigit():\n",
    "        print(\"Please enter digits only.\")\n",
    "        continue\n",
    "    b = int(b)\n",
    "    if b == 0:\n",
    "        print(\"Exiting system… Stay safe!\")\n",
    "        break\n",
    "    # Calculate GCD using repeated subtraction method\n",
    "    x, y = a, b\n",
    "    while x != y:\n",
    "        if x > y:\n",
    "            x = x - y\n",
    "        else:\n",
    "            y = y - x\n",
    "    gcd = x\n",
    "    print(\"GCD of\", a, \"and\", b, \"is:\", gcd)\n",
    "    # Police alert based on GCD result\n",
    "    if gcd >= 10:\n",
    "        print(\"Police: High Alert Triggered based on GCD result!\")\n",
    "        break\n",
    "    elif gcd >= 5:\n",
    "        print(\"Police: Moderate Alert. Monitoring the situation.\\n\")\n",
    "    else:\n",
    "        print(\"Police: Low Alert. Woman may continue sending values.\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d41278bb-b681-4c63-935c-a83d287517b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WOMEN SAFETY SYSTEM – FIBONACCI ALERT\n",
      "Enter two positions of Fibonacci series.\n",
      "Enter 0 anytime to stop.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first Fibonacci position:  4\n",
      "Enter second Fibonacci position:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci at position 4 = 3\n",
      "Fibonacci at position 7 = 13\n",
      "Combined Alert Value = 16\n",
      "Police: Moderate Alert. Stay calm.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first Fibonacci position:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting system… Stay safe!\n"
     ]
    }
   ],
   "source": [
    "# Women Safety Alert System using Fibonacci Series\n",
    "\n",
    "print(\"WOMEN SAFETY SYSTEM – FIBONACCI ALERT\")\n",
    "print(\"Enter two positions of Fibonacci series.\")\n",
    "print(\"Enter 0 anytime to stop.\\n\")\n",
    "\n",
    "while True:\n",
    "    a = input(\"Enter first Fibonacci position: \")\n",
    "\n",
    "    if a == \"\":\n",
    "        print(\"Error: Input cannot be empty.\")\n",
    "        continue\n",
    "\n",
    "    if not a.isdigit():\n",
    "        print(\"Please enter numbers only.\")\n",
    "        continue\n",
    "\n",
    "    a = int(a)\n",
    "    if a == 0:\n",
    "        print(\"Exiting system… Stay safe!\")\n",
    "        break\n",
    "\n",
    "    b = input(\"Enter second Fibonacci position: \")\n",
    "\n",
    "    if b == \"\":\n",
    "        print(\"Error: Input cannot be empty.\")\n",
    "        continue\n",
    "\n",
    "    if not b.isdigit():\n",
    "        print(\"Please enter numbers only.\")\n",
    "        continue\n",
    "\n",
    "    b = int(b)\n",
    "    if b == 0:\n",
    "        print(\"Exiting system… Stay safe!\")\n",
    "        break\n",
    "\n",
    "    # Function to compute Fibonacci number at position n\n",
    "    def fib(n):\n",
    "        if n == 1 or n == 2:\n",
    "            return 1\n",
    "        f1, f2 = 1, 1\n",
    "        for _ in range(3, n + 1):\n",
    "            f3 = f1 + f2\n",
    "            f1 = f2\n",
    "            f2 = f3\n",
    "        return f2\n",
    "\n",
    "    fib_a = fib(a)\n",
    "    fib_b = fib(b)\n",
    "\n",
    "    print(\"Fibonacci at position\", a, \"=\", fib_a)\n",
    "    print(\"Fibonacci at position\", b, \"=\", fib_b)\n",
    "\n",
    "    # Combined alert value\n",
    "    alert = fib_a + fib_b\n",
    "    print(\"Combined Alert Value =\", alert)\n",
    "\n",
    "    # Police Alert Levels\n",
    "    if alert >= 50:\n",
    "        print(\"Police: EXTREME DANGER! Rushing Immediately!\")\n",
    "        break\n",
    "    elif alert >= 20:\n",
    "        print(\"Police: High Alert! Moving towards location.\\n\")\n",
    "    elif alert >= 10:\n",
    "        print(\"Police: Moderate Alert. Stay calm.\\n\")\n",
    "    else:\n",
    "        print(\"Police: Low Alert. Monitoring… Woman can send again.\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "888818ae-eca6-4c68-ba5f-0936404d0794",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WOMEN SAFETY SYSTEM – ARRAY BASED ALERT\n",
      "Woman will enter multiple alert values in an array.\n",
      "System will check strongest alert and notify police.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter alert values separated by space (or 0 to quit):  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Alert array = [8]\n",
      "Highest Alert = 8\n",
      "Police: HIGH Alert! Officers moving now.\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter alert values separated by space (or 0 to quit):  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "System exiting… Stay Safe!\n"
     ]
    }
   ],
   "source": [
    "# Women Safety Alert System using Arrays\n",
    "\n",
    "print(\"WOMEN SAFETY SYSTEM – ARRAY BASED ALERT\")\n",
    "print(\"Woman will enter multiple alert values in an array.\")\n",
    "print(\"System will check strongest alert and notify police.\\n\")\n",
    "\n",
    "while True:\n",
    "    data = input(\"Enter alert values separated by space (or 0 to quit): \")\n",
    "\n",
    "    if data == \"\":\n",
    "        print(\"Error: Input cannot be empty.\")\n",
    "        continue\n",
    "\n",
    "    # If user wants to exit\n",
    "    if data.strip() == \"0\":\n",
    "        print(\"System exiting… Stay Safe!\")\n",
    "        break\n",
    "\n",
    "    # Convert input to array\n",
    "    parts = data.split()\n",
    "    alerts = []\n",
    "\n",
    "    valid = True\n",
    "    for p in parts:\n",
    "        if not p.isdigit():\n",
    "            valid = False\n",
    "            break\n",
    "        alerts.append(int(p))\n",
    "\n",
    "    if not valid:\n",
    "        print(\"Please enter numbers only.\")\n",
    "        continue\n",
    "\n",
    "    print(\"Alert array =\", alerts)\n",
    "\n",
    "    # Find maximum alert value in array\n",
    "    max_alert = alerts[0]\n",
    "    for val in alerts:\n",
    "        if val > max_alert:\n",
    "            max_alert = val\n",
    "\n",
    "    print(\"Highest Alert =\", max_alert)\n",
    "\n",
    "    # Police Response Conditions\n",
    "    if max_alert >= 9:\n",
    "        print(\"Police: EXTREME Danger! Rushing Immediately!\")\n",
    "        break\n",
    "    elif max_alert >= 6:\n",
    "        print(\"Police: HIGH Alert! Officers moving now.\\n\")\n",
    "    elif max_alert >= 3:\n",
    "        print(\"Police: MODERATE Alert. Stay calm.\\n\")\n",
    "    else:\n",
    "        print(\"Police: LOW Alert. Monitoring situation…\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e5b758c-e31f-4adf-9022-ac7c6c291330",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
