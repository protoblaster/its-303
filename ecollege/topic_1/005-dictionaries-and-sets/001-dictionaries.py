{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8684000d",
   "metadata": {},
   "source": [
    "### Dictionary ---> A mapping of Key:Value pairs\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "059de4cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "empty_dict = {}\n",
    "empty_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4567f7da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'James': 'Ducati Monster 1200',\n",
       " 'Jacob': 'Ducati Scrambler 1100',\n",
       " 'William': 'BMW s 1000 RR',\n",
       " 'Aiden': 'Harley Davidson'}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A dictionary contains key:value pairs\n",
    "bike_owners = {\"James\" : \"Ducati Monster 1200\",\n",
    "              \"Jacob\" : \"Ducati Scrambler 1100\",\n",
    "              \"William\" : \"BMW s 1000 RR\",\n",
    "              \"Aiden\" : \"Harley Davidson\"}\n",
    "bike_owners"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "af492f92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Ducati Monster 1200'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bike_owners[\"James\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d973feb0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The most common data types used for keys in dictionaries \n",
    "# are strings but integers can also be used\n",
    "\n",
    "int_dict = {1 : 45, 2 : 55, 3 : 65}\n",
    "int_dict[1]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef84e0d5",
   "metadata": {},
   "source": [
    "### NOTE: Keys in dictionaries must be unique\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ffbb64eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Henry': 1995, 'Samuel': 1999, 'Ingrid': 2005}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student_details = {\"Henry\" : 1995,\n",
    "                  \"Samuel\" : 1999,\n",
    "                  \"Ingrid\" : 2005}\n",
    "student_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7f9fbc9a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['Henry', 'Samuel', 'Ingrid'])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# print the keys in dictionary\n",
    "student_details.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9297bc3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"Samuel\" in student_details.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "4ac6b430",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"Andrew\" in student_details.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "248518f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([1995, 1999, 2005])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# print the values of dictionary\n",
    "student_details.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6e992583",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{False: 'Daniel', 'Aria': [1, 2, 3], 'Jacob': True}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mixed_dict = {False : \"Daniel\",\n",
    "             \"Aria\" : [1, 2, 3],\n",
    "             \"Jacob\" : True}\n",
    "mixed_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "968f10c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Daniel'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mixed_dict[\"Aria\"]\n",
    "mixed_dict[False]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "204a11c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bike_owner': 'James Smith',\n",
       " 'bike_model': 'Ducati Monster 1200',\n",
       " 'bike_price': 28140,\n",
       " 'engine_displacement': 1997}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bike_details = {\"bike_owner\" : \"James Smith\",\n",
    "               \"bike_model\" : \"Ducati Monster 1200\",\n",
    "               \"bike_price\" : 28140,\n",
    "               \"engine_displacement\" : 1997}\n",
    "bike_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "bd4ebf92",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bike_owner': 'James Smith',\n",
       " 'bike_model': 'Ducati Monster 1200',\n",
       " 'bike_price': 28140,\n",
       " 'engine_displacement': 1997,\n",
       " 'num_cylinders': 2}"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create a new key value pair\n",
    "bike_details[\"num_cylinders\"] = 2\n",
    "bike_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0a53d4e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bike_owner': 'James Smith',\n",
       " 'bike_model': 'Ducati Monster 1200',\n",
       " 'bike_price': 29140,\n",
       " 'engine_displacement': 1997,\n",
       " 'num_cylinders': 2}"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# update the price of the bike\n",
    "bike_details[\"bike_price\"] = 29140\n",
    "bike_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "eb485055",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29140"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bike_details.get(\"bike_price\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d307f0ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'bike_owner': 'James Smith',\n",
       " 'bike_model': 'Ducati Monster 1200',\n",
       " 'bike_price': 29140,\n",
       " 'num_cylinders': 2}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# dictionaries are mutable (meaning that they can be changed)\n",
    "del bike_details[\"engine_displacement\"]\n",
    "bike_details"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b91cd3a4",
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
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
