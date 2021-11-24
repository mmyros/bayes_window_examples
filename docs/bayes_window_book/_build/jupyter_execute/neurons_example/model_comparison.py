#!/usr/bin/env python
# coding: utf-8

# # Compare to alternative models

# In[1]:



from bayes_window.generative_models import generate_fake_spikes
from bayes_window.model_comparison import *
from bayes_window import BayesWindow


# In[2]:


df, df_monster, index_cols, firing_rates = generate_fake_spikes(n_trials=140,
                                                                n_neurons=10,
                                                                n_mice=8,
                                                                dur=7, 
                                                               mouse_response_slope=20,
                                                               overall_stim_response_strength=4)


# ## Bayesian

# In[3]:


window = BayesWindow(df, y='isi', treatment='stim', group='mouse', condition='neuron')
window.fit_slopes(model=models.model_hierarchical, do_mean_over_trials=True,)
window.explore_models()


# Simple one-way ANOVA:

# In[4]:


window.fit_anova()


# ## Linear mixed effects model

# In[7]:


window = BayesWindow(df, y='isi', treatment='stim', group='mouse', condition='neuron_x_mouse')
window.fit_lme()
window.posterior


# In[9]:


window.plot(x='neuron_x_mouse')


# Of course in reality, neurons don't have this consistent variation in each mouse. This would only be applicable to a priori classes of neurons
