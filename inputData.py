import numpy as np
import pandas as pd

dataPath = '/Users/omojumiller/Dropbox/Research/DissertationSubmission/'

cs10Spring_df = pd.read_csv(dataPath+'Data/CS10_Pre_Responses_Spring2015.csv') 
cs10Spring_pdf = pd.read_csv(dataPath+'Data/CS10_Post_Responses_Spring2015.csv')
cs61a = pd.read_csv(dataPath+'Data/CS61A_Responses_Fall2014.csv')

## Column names
cs10Spring_df.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1', 'name_2']

cs10Spring_pdf.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1',
                            'snap_python','hiphop_d1','hiphop_d2','song_ct']

cs61a.columns = ['timestamp','consent','gender',
'reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1','atcs_3','atcs_4',
'atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3','atct_1',
'atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1','cltrcmp_2','classmtr',
'prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','priorcs10','name']


def process( cs61a, cs10Spring_df, cs10Spring_pdf  ):

    ## Preparing the Data
    ## In this section, I will prepare the data for modeling, training and testing.

    ## Identify feature and target columns
    ## It is often the case that ones data contains non-numeric features. 
    ## This can be a problem, as most machine learning algorithms expect numeric data to perform computations with.

    ## Let's first separate our data into feature and target columns, and see if any features are non-numeric.<br/>
    ## **Note**: For this dataset, the column (`'gender'`) is the target or label we are trying to predict.
    ## - Only use rows where students have given consent
    ## - Only use rows where we have values for gender that are either `"male"` or `"female"`

    ## Lets go ahead and filter out missing data. 
    ## If the consent value is "I disagree", then drop that row from the data set.

    cs61a = cs61a[cs61a.consent == 'I agree']
    cs10Spring_df = cs10Spring_df[cs10Spring_df.consent == 'I agree']
    cs10Spring_pdf = cs10Spring_pdf[cs10Spring_pdf.consent == 'I agree']

    ## Combine all the different data samples representing the two collections from CS10 and the one collection from 61a

    frames = [cs10Spring_df, cs10Spring_pdf, cs61a]
    student_data = pd.concat(frames, keys=['pre', 'post','61a'])

    return student_data

def preprocess():
    return process( cs61a, cs10Spring_df, cs10Spring_pdf  )
    


