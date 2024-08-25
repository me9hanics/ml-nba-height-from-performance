# NBA Height Prediction from Performance

Machine learning models used to predict the height of basketball players, from playstyle and performance statistics. Data collected using the `nba_api` package, of the previous 20 seasons.

- Models: Gradient boosted regressors and classifiers, random forests
- Data analysis: Clustering, preparing clean data for better performance.

The results show, that two regressors (one gradient boosted, and a random forest regressor) can predict the height of a player **within 1 inch 50% of the time**. Moreover, on the data the latter model predicted inside the (-7, 5) inch error range for every player; predicting inside +-2 inches for 72.9% of the players, and +-3 inches for 86.4% of the players.

**Preprocessing, analysis, prediction:**: inside the `ml.ipynb` notebook<br> 
**Data collection, some cleaning**: described in `fetch_players.ipynb`.

**Data** is stored in the `data` folder.

A summary of the best models:

| Model                                                | Data | Accuracy Score | +/-1 inch % | +/-2 inch % | +/-3 inch % | F1 Score | Error Range   |
|------------------------------------------------------|------|----------------|-------------|-------------|-------------|----------|---------------|
| Random forest: best classifier                             | All  | **17.6%**      | 45.3%       | 70.3%       | 83.7%       | **0.155**| -8 , 6        |
| Ensembled (manually biased) forest                            | All  | 16.2%          | **49.0%**   | **71.3%**   | **85.4%**   | 0.149    | -8 , 5        |
| Random forest: best regressor                              | All  | -              | **50.0%**   | **72.9%**   | **86.4%**   | -        | **-7 , 5**    |
| Best gradient boosted regressor       | All  | -              | **49.9%**   | 69.1%       | 84.5%       | -        | -8 , 6        |

The pipeline picture:

<div style="text-align: center;">
    <img src="img/pipeline.svg" title="NBA player height prediction from performance and playstyle - Pipeline" height="500"/>
</div>


# How..

## to run?

I recommend to just download (clone) the whole repository.

The dependencies are listed in the `requirements.in` and the `requirements.txt` file.<br>
After downloading the repository, in your command line shell go to this directory, choose/create a `Python`/`conda`/`virtualenv` environment and run `pip install -r requirements.txt`.<br>
If you want to fetch the data yourself (which is already fetched and stored in the `data` folder), you additionally need to run `pip install nba_api` to use the package, in the `fetch_players.ipynb` notebook.<br>



## Results table

| Model                                                | Data | Accuracy Score | +/-1 inch % | +/-2 inch % | +/-3 inch % | F1 Score | Error Range   |
|------------------------------------------------------|------|----------------|-------------|-------------|-------------|----------|---------------|
| Decision tree                                        | All  | 15.7%          | 42.8%       | 67.7%       | 81.3%       | 0.154    | -8 , 7        |
| Random forest classifier                             | All  | **17.6%**      | 45.3%       | 70.3%       | 83.7%       | **0.155**    | -8 , 6        |
| Ensemble forest 1                                    | All  | 15.5%          | 44.9%       | 70.2%       | 83.0%       | 0.137    | -8 , 6        |
| Ensemble forest averaging                            | All  | 16.2%          | **49.0%**   | **71.3%**   | **85.4%**   | 0.149    | -8 , 5        |
| Random forest regressor                              | All  | -              | **50.0%**   | **72.9%**   | **86.4%**   | -        | **-7 , 5**    |
| Gradient boosted classifier, no tuning, previous parameters | All  | 17.1%   | 44.5        | 64.9%       | 78.9%       | 0.169    | -14 , 9       |
| Gradient boosted classifier, with hyperparameter tuning| All| 15.2%          | 41.6%       | 65.7%       | 79.3%       | 0.131    | -8 , 12       |
| Gradient boosted classifier, with tuning, initialized from RF| All | 15.8%   | 43.5%       | 67.4%       | 81.3%       | 0.148    | -8 , 6        |
| Gradient boosted regressor (from the RF model)       | All  | -              | **49.9%**       | 69.1%       | 84.5%       | -        | -8 , 6        |
| Gradient boosted classifier, with shuffled data  | Shuffled | 8.8%           | 28.1%       | 43.4%       | 59.8%       | 0.087    | -14 , 11      |
| Gradient boosted regressor, with shuffled data   | Shuffled | -              | 38.6%       | 67.1%       | 82.8%       | -        | -12 , 6       |

The gradient boosted methods underperformed likely because of lack of data, and the scikit-learn implementation not being state of the art (like XGBoost).<br>
**Classifiers**: In **accuracy**, only are used for evaluation, and the **random forest classifier** does the best with **17.6%** (and had the highest F-score), only the gradient boosted classifier initialized from its parameters manages to go above 17% accuracy. The **averaging ensemble forest method** however had the **best scores in all other categories (+-N inch ranges, error range)**, and came close to the best regressor method in all categories.<br>
**Regresssors**: We find that random forest regressor works, as the only model hitting **50% accuracy in the +-1 inch range**. It also hits the highest score in all other categories: **72.9% +-2 inch accuracy, 86.4% +-3 inch accuracy, and -7,5 error range**. Among the gradient boosted regressors, only the regressor initialized from the random forest does comparably, with 49.9% accuracy in +-1 inch range. <br>

This means, that the random forest regressor can **predict the height of a player within 1 inch half of the time**. This is a strong result for such a noisy problem.<br>

We also see that it is better to train the model with players not appearing in both train and test datasets.<br>

Outdated summary [pdf file](https://github.com/me9hanics/ml-nba-height-from-performance/blob/main/ml-nba-height-from-performance.pdf) for overall explanation.


