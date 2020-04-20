import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1.2.1 we define the variable for lab quality
labs_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'labs')
labs_quality.automf(3)

labs_quality.view()
plt.show()

# 1.2.1 we define the variable for lecture quality
lecture_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'lectures')
lecture_quality.automf(3)

# 1.2.2 we define the variable for course rating
rating = ctrl.Consequent(np.arange(0, 11, 1), 'rating')

# 1.2.2 we define the fuzzy values manually
rating['low'] = fuzz.trimf(rating.universe, [0, 0, 5])
rating['medium'] = fuzz.trimf(rating.universe, [0, 5, 10])
rating['high'] = fuzz.trimf(rating.universe, [5, 10, 10])

rating.view()
plt.show()

# 1.3 we define all rules
rule1 = ctrl.Rule(
    labs_quality['poor'] | lecture_quality['poor'],
    rating['low'])
rule2 = ctrl.Rule(
    labs_quality['average'],
    rating['medium'])
rule3 = ctrl.Rule(
    lecture_quality['good'] & labs_quality['good'],
    rating['high'])

# 1.4 we define the fuzzy control system
rating_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# 1.5 we define a testing scenario and visualize the result
my_rating = ctrl.ControlSystemSimulation(rating_ctrl)

my_rating.input['labs'] = 6.5
my_rating.input['lectures'] = 9.8

my_rating.compute()
print("The suggested rating is {:.2f}".format(my_rating.output['rating']))

rating.view(sim=my_rating)
plt.show()
