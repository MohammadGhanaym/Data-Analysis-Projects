### Introduction

>In this project, we'll be analyzing Movies data.
In particular, we'll be interested in knowing which genres are most popular from year to year? What kinds of properties are associated with movies that have high revenues? We will dig into this data to answer these questions.
This data set contains information about 10866 movies, including user ratings and revenue

**columns in this data set:**
- id
- imdb_id
- popularity
- budget
- revenue
- original_title
- cast
- homepage
- director
- tagline
- keywords
- overview
- runtime
- genres
- production_companies
- release_date
- vote_count
- vote_average
- release_year
- budget_adj
- revenue_adj


### Questions to answer
1. Which genre has the highest number of movies?
2. Which year has the highest number of moveis?
3. What is the relation between number of years and movies?
4. Which production company released the most number movies over the years?
5. How long time do movies take on average?
6. What is the relationship between popularity and vote count?
7. Does a bigger film production budget result in more revenue and popularity?
8. What is the status of movies rating over the years?
9. Which genres are most popular from year to year?
10. What kinds of properties are associated with movies that have high revenues?

### Conclusions
After digging deep into these data, do some statistical analysis, and answer some question, here they are the insights I got:  
- Most of the movies in this dataset are comedy and drama movies.
- In 2011 over 175 movies have been released, and this the most number of movies released in a specific year.
- The number of movies increases over years.
- Paramount Pictures company has released the most number of movies.
- These movies take 109.35 minute on average.
- The popularity and revenue are increases with the budget of the movie. The more budget is, the more popularity and revenue are
- The average rating of movies is getting worse over the years, which means the old movies get high ratings than the new ones.
- From 1960 to 1995, the most popular genres is Action|Adventure|Science Fiction|Thriller
- From 1995 to 2004, the most popular genres is Adventure|Action|Science Fiction
- From 2004 to 2010, the most popular genres is Action|Thriller|Science Fiction|Mystery|Adventure
- From 2010 to 2015, the most popular genres is Fantasy|Action|Thriller
- Action|Adventure|Science Fiction|Thriller is the most popular genres in all intervals.
- The increase in vote count causes an increase in popularity.
- **The properties of movies that have high revenue**

   - Most of these movies are produced by Paramount Pictures.
   - Most of the movies are released in the interval from 1995 to 2011.
   - Most of these movies are directed by Steven Spielberg.
   - The movies have a high budget.
   - Runtime doesn't exceed 201 and not less than 72.
   - The vote count doesn't exceed 9767 and this is the maximum number of the vote counts.
   
 **Limitations**
- All insights are limited to the underlying data set, and they can't be generalized. Taking into account, a large number of entries have been removed due to missing values.
