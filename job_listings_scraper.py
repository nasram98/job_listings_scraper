{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "02a7a58b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup as BS\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "04ffbca4",
   "metadata": {},
   "outputs": [],
   "source": [
    "URL = 'https://realpython.github.io/fake-jobs/'\n",
    "response = requests.get(URL)\n",
    "soup = BS(response.text, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "13529eb7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Successfully retrieved the webpage.\n"
     ]
    }
   ],
   "source": [
    "if response.status_code == 200:\n",
    "    print(\"Successfully retrieved the webpage.\")\n",
    "else:\n",
    "    print(f\"Failed to retrieve the webpage. Status code: {response.status_code}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "94718120",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     Title                     Company              Location  \\\n",
      "0  Senior Python Developer    Payne, Roberts and Davis       Stewartbury, AA   \n",
      "1          Energy engineer            Vasquez-Davidson  Christopherville, AA   \n",
      "2          Legal executive  Jackson, Chambers and Levy   Port Ericaburgh, AA   \n",
      "3   Fitness centre manager              Savage-Bradley     East Seanview, AP   \n",
      "4          Product manager                 Ramirez Inc   North Jamieview, AP   \n",
      "\n",
      "         Date                                               Link  \n",
      "0  2021-04-08  https://realpython.github.io/fake-jobs/jobs/se...  \n",
      "1  2021-04-08  https://realpython.github.io/fake-jobs/jobs/en...  \n",
      "2  2021-04-08  https://realpython.github.io/fake-jobs/jobs/le...  \n",
      "3  2021-04-08  https://realpython.github.io/fake-jobs/jobs/fi...  \n",
      "4  2021-04-08  https://realpython.github.io/fake-jobs/jobs/pr...  \n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup as BS\n",
    "import pandas as pd\n",
    "\n",
    "URL = 'https://realpython.github.io/fake-jobs/'\n",
    "response = requests.get(URL)\n",
    "soup = BS(response.text, 'lxml')\n",
    "\n",
    "job_titles = [title.text.strip() for title in soup.find_all('h2', class_='title')]\n",
    "\n",
    "companies = [company.text.strip() for company in soup.find_all('h3', class_='company')]\n",
    "\n",
    "locations = [location.text.strip() for location in soup.find_all('p', class_='location')]\n",
    "\n",
    "posting_dates = [date.text.strip() for date in soup.find_all('time')]\n",
    "\n",
    "apply_links = []\n",
    "for s in soup.find_all('a', href=True):\n",
    "    if s.text == 'Apply':\n",
    "        apply_links.append(s['href'])\n",
    "\n",
    "postings = pd.DataFrame({\n",
    "    'Title': job_titles,\n",
    "    'Company': companies,\n",
    "    'Location': locations,\n",
    "    'Date': posting_dates,\n",
    "    'Link': apply_links\n",
    "})\n",
    "\n",
    "print(postings.head())\n",
    "postings.to_csv('job_postings.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "765b2550",
   "metadata": {},
   "source": [
    "Finally, we want to get the job description text for each job.\n",
    "a. Start by looking at the page for the first job, https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html. Using BeautifulSoup, extract the job description paragraph."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "13a5887a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Job Description: Fake Jobs for Your Web Scraping Journey\n"
     ]
    }
   ],
   "source": [
    "post1_url = 'https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html'\n",
    "post1_response = requests.get(post1_url)\n",
    "post1_soup = BS(post1_response.text, 'lxml')\n",
    "job_description = post1_soup.find('p').text.strip() \n",
    "print(\"Job Description:\", job_description)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1d1b1203",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Professional asset web application environmentally friendly detail-oriented asset. Coordinate educational dashboard agile employ growth opportunity. Company programs CSS explore role. Html educational grit web application. Oversea SCRUM talented support. Web Application fast-growing communities inclusive programs job CSS. Css discussions growth opportunity explore open-minded oversee. Css Python environmentally friendly collaborate inclusive role. Django no experience oversee dashboard environmentally friendly willing to learn programs. Programs open-minded programs asset.'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "post1_soup.find_all('p')[1].text.strip()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2346d5b2",
   "metadata": {},
   "source": [
    "b. Write a function which takes as input a url and returns the description text on that page."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d15f2415",
   "metadata": {},
   "outputs": [],
   "source": [
    "def job_description(post_url):\n",
    "    post_response = requests.get(post_url)\n",
    "    post_soup = BS(post_response.text, 'lxml')\n",
    "    return post_soup.find_all('p')[1].text.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2057535d",
   "metadata": {},
   "outputs": [],
   "source": [
    "postings['Description'] = postings['Link'].apply(job_description)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8377cd6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     Title                     Company  \\\n",
      "0  Senior Python Developer    Payne, Roberts and Davis   \n",
      "1          Energy engineer            Vasquez-Davidson   \n",
      "2          Legal executive  Jackson, Chambers and Levy   \n",
      "3   Fitness centre manager              Savage-Bradley   \n",
      "4          Product manager                 Ramirez Inc   \n",
      "\n",
      "                                         Description  \n",
      "0  Professional asset web application environment...  \n",
      "1  Party prevent live. Quickly candidate change a...  \n",
      "2  Administration even relate head color. Staff b...  \n",
      "3  Tv program actually race tonight themselves tr...  \n",
      "4  Traditional page a although for study anyone. ...  \n"
     ]
    }
   ],
   "source": [
    "def job_description(post_url):\n",
    "    post_response = requests.get(post_url)\n",
    "    post_soup = BS(post_response.text, 'lxml')\n",
    "    paragraphs = post_soup.find_all('p')\n",
    "    if len(paragraphs) > 1:\n",
    "        return paragraphs[1].text.strip()\n",
    "    else:\n",
    "        return \"Description not found.\"\n",
    "\n",
    "postings['Description'] = postings['Link'].apply(job_description)\n",
    "\n",
    "# Display the updated DataFrame with descriptions\n",
    "print(postings[['Title', 'Company', 'Description']].head())\n",
    "\n",
    "# Save the DataFrame to a CSV file (optional)\n",
    "postings.to_csv('job_postings_with_descriptions.csv', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c188f2e4",
   "metadata": {},
   "source": [
    "Now I am going to Use the .apply method on the url column you created above to retrieve the description text for all of the jobs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a343944e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Title</th>\n",
       "      <th>Company</th>\n",
       "      <th>Location</th>\n",
       "      <th>Date</th>\n",
       "      <th>Link</th>\n",
       "      <th>Description</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Senior Python Developer</td>\n",
       "      <td>Payne, Roberts and Davis</td>\n",
       "      <td>Stewartbury, AA</td>\n",
       "      <td>2021-04-08</td>\n",
       "      <td>https://realpython.github.io/fake-jobs/jobs/se...</td>\n",
       "      <td>Professional asset web application environment...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Energy engineer</td>\n",
       "      <td>Vasquez-Davidson</td>\n",
       "      <td>Christopherville, AA</td>\n",
       "      <td>2021-04-08</td>\n",
       "      <td>https://realpython.github.io/fake-jobs/jobs/en...</td>\n",
       "      <td>Party prevent live. Quickly candidate change a...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Legal executive</td>\n",
       "      <td>Jackson, Chambers and Levy</td>\n",
       "      <td>Port Ericaburgh, AA</td>\n",
       "      <td>2021-04-08</td>\n",
       "      <td>https://realpython.github.io/fake-jobs/jobs/le...</td>\n",
       "      <td>Administration even relate head color. Staff b...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Fitness centre manager</td>\n",
       "      <td>Savage-Bradley</td>\n",
       "      <td>East Seanview, AP</td>\n",
       "      <td>2021-04-08</td>\n",
       "      <td>https://realpython.github.io/fake-jobs/jobs/fi...</td>\n",
       "      <td>Tv program actually race tonight themselves tr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Product manager</td>\n",
       "      <td>Ramirez Inc</td>\n",
       "      <td>North Jamieview, AP</td>\n",
       "      <td>2021-04-08</td>\n",
       "      <td>https://realpython.github.io/fake-jobs/jobs/pr...</td>\n",
       "      <td>Traditional page a although for study anyone. ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Title                     Company              Location  \\\n",
       "0  Senior Python Developer    Payne, Roberts and Davis       Stewartbury, AA   \n",
       "1          Energy engineer            Vasquez-Davidson  Christopherville, AA   \n",
       "2          Legal executive  Jackson, Chambers and Levy   Port Ericaburgh, AA   \n",
       "3   Fitness centre manager              Savage-Bradley     East Seanview, AP   \n",
       "4          Product manager                 Ramirez Inc   North Jamieview, AP   \n",
       "\n",
       "         Date                                               Link  \\\n",
       "0  2021-04-08  https://realpython.github.io/fake-jobs/jobs/se...   \n",
       "1  2021-04-08  https://realpython.github.io/fake-jobs/jobs/en...   \n",
       "2  2021-04-08  https://realpython.github.io/fake-jobs/jobs/le...   \n",
       "3  2021-04-08  https://realpython.github.io/fake-jobs/jobs/fi...   \n",
       "4  2021-04-08  https://realpython.github.io/fake-jobs/jobs/pr...   \n",
       "\n",
       "                                         Description  \n",
       "0  Professional asset web application environment...  \n",
       "1  Party prevent live. Quickly candidate change a...  \n",
       "2  Administration even relate head color. Staff b...  \n",
       "3  Tv program actually race tonight themselves tr...  \n",
       "4  Traditional page a although for study anyone. ...  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "postings['Description'] = postings['Link'].apply(job_description)\n",
    "postings.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83dd0bb5",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
