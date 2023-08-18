{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3f04a173 ",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dead6fc2 ",
   "metadata": {},
   "outputs": [],
   "source": [
    "movies=pd.read_csv('dataset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5b1a49bf ",
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
       "      <th>anime_id</th>\n",
       "      <th>name</th>\n",
       "      <th>genre</th>\n",
       "      <th>type</th>\n",
       "      <th>episodes</th>\n",
       "      <th>rating</th>\n",
       "      <th>members</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>32281</td>\n",
       "      <td>Kimi no Na wa /td>\n",
       "      <td>Drama; Romance; School; Supernatural</td>\n",
       "      <td>Movie</td>\n",
       "      <td>1</td>\n",
       "      <td>9.37 </td>\n",
       "      <td>200630 </td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5114</td>\n",
       "      <td>Fullmetal Alchemist: Brotherhood</td>\n",
       "      <td>Action; Adventure; Drama; Fantasy; Magic; Military; Shounen</td>\n",
       "      <td>TV</td>\n",
       "      <td>64</td>\n",
       "      <td>9.26</td>\n",
       "      <td>793665</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>28977</td>\n",
       "      <td>Gintama</td>\n",
       "      <td>Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen</td>\n",
       "      <td>TV</td>\n",
       "      <td>51</td>\n",
       "      <td>9.25</td>\n",
       "      <td>114262</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>9253</td>\n",
       "      <td>Steins;Gate</td>\n",
       "      <td>Sci-Fi; Thriller</td>\n",
       "      <td>TV</td>\n",
       "      <td>24</td>\n",
       "      <td>9.17</td>\n",
       "      <td>673572</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9969</td>\n",
       "      <td>Gintama</td>\n",
       "      <td>Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen</td>\n",
       "      <td>TV</td>\n",
       "      <td>51</td>\n",
       "      <td>9.16</td>\n",
       "      <td>151266</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>32935</td>\n",
       "      <td>Haikyuu!! Karasuno Koukou VS Shiratorizawa Gakuen Koukou</td>\n",
       "      <td>Comedy; Drama; School; Shounen; Sports</td>\n",
       "      <td>TV</td>\n",
       "      <td>10</td>\n",
       "      <td>9.15</td>\n",
       "      <td>93351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>11061</td>\n",
       "      <td>Hunter x Hunter (2011)</td>\n",
       "      <td>Drama; Military; Sci-Fi; Space</td>\n",
       "      <td>TV</td>\n",
       "      <td>148</td>\n",
       "      <td>9.13</td>\n",
       "      <td>425855</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>820</td>\n",
       "      <td>Ginga Eiyuu Densetsu</td>\n",
       "      <td>Drama; Military; Sci-Fi; Space</td>\n",
       "      <td>OVA</td>\n",
       "      <td></td>\n",
       "      <td>9.11</td>\n",
       "      <td>80679</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>15335</td>\n",
       "      <td>Gintama Movie: Kanketsu-hen - Yorozuya yo Eien Nare</td>\n",
       "      <td>Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen</td>\n",
       "      <td>Movie</td>\n",
       "      <td>1</td>\n",
       "      <td>9.1</td>\n",
       "      <td>72534</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>15417</td>\n",
       "      <td>Gintama: Enchousen</td>\n",
       "      <td>Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen</td>\n",
       "      <td>TV</td>\n",
       "      <td>13</td>\n",
       "      <td>9.11</td>\n",
       "      <td>81109</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
        ],
      "text/plain": [
       "0    anime_id                                                           name                                                                 genre  \\\n",
       "1       32281                                                  Kimi no Na wa                                  Drama; Romance; School; Supernatural   \n",
       "2        5114                               Fullmetal Alchemist: Brotherhood           Action; Adventure; Drama; Fantasy; Magic; Military; Shounen   \n",
       "3       28977                                                        Gintama          Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen   \n",
       "4        9253                                                    Steins;Gate                                                      Sci-Fi; Thriller   \n",
       "5        9969                                                        Gintama          Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen   \n",
       "6       32935       Haikyuu!! Karasuno Koukou VS Shiratorizawa Gakuen Koukou                                Comedy; Drama; School; Shounen; Sports   \n",
       "7       11061                                         Hunter x Hunter (2011)                               Action; Adventure, Shounen, Super Power   \n",
       "8         820                                           Ginga Eiyuu Densetsu                                        Drama; Military; Sci-Fi; Space   \n",
       "9       15335            Gintama Movie: Kanketsu-hen - Yorozuya yo Eien Nare          Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen   \n",
       "10      15417                                             Gintama: Enchousen          Action; Comedy; Historical; Parody; Samurai; Sci-Fi; Shounen   \n",
       "\n",
       "  type                           episodes  \\\n",
       "1             Movie                     1   \n",
       "2                TV                    64   \n",
       "3                TV                    51  \n",
       "4                TV                    24   \n",
       "5                TV                    51   \n",
       "6                TV                    10   \n",
       "7                TV                   148   \n",
       "8               OVA                   110   \n",
       "9             Moive                     1   \n",
       "10               TV                    13   \n",
       "\n",
       "       rating               members   \n",
       "1      9.37                  200630   \n",
       "2      9.26                  793665   \n",
       "3      9.25                  114262   \n",
       "4      9.17                  673572   \n",
       "5      9.16                  151266   \n",
       "6      9.15                   93351   \n",
       "7      9.13                  425855   \n",
       "8      9.11                   80679   \n",
       "9      9.1                    72534   \n",
       "10     9.11                   81109   "
      ]
       },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movies.head(10)"
   ]
  },