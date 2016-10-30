import numpy as np
import pandas as pd
import pickle 
import scipy.stats as stats


dataPath = '/Users/omojumiller/Dropbox/Research/DissertationSubmission/'


CS10SPRING_DATA_1 = pd.read_csv(dataPath+'Data/CS10_Pre_Responses_Spring2015.csv')
CS10SPRING_DATA_2 = pd.read_csv(dataPath+'Data/CS10_Post_Responses_Spring2015.csv')
CS61A_DATA = pd.read_csv(dataPath+'Data/CS61A_Responses_Fall2014.csv')

## Column names
CS10SPRING_DATA_1.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1', 'name_2']

CS10SPRING_DATA_2.columns = ['timestamp',
'consent','gender','reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1',
'atcs_3','atcs_4','atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3',
'atct_1','atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1',
'cltrcmp_2','classmtr','prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','name_1',
                            'snap_python','hiphop_d1','hiphop_d2','song_ct']

CS61A_DATA.columns = ['timestamp','consent','gender',
'reason_class','major','atcs_1','atcsjob_1','atcs_2','atcsjob_2','atcsgender_1','atcs_3','atcs_4',
'atcs_5','atcsgender_2','atcs_6','atcs_7','atcs_8','atcs_9','atcsgender_3','atct_1',
'atct_2','atct_3','atct_4','atct_5','atct_6','atct_7','atct_8','clet_1','clet_2','grade',
'mtr_1','mtr_2','mtr_3','blg_1','blg_2','blg_3','blg_4','cltrcmp_1','cltrcmp_2','classmtr',
'prcs_1','prcs_2','prcs_3','prcs_4','prcs_5','prepared','morecs','priorcs10','name']



dd = pd.read_csv(dataPath+'Data/Data_Describe.csv')
dd.columns = ['dataDecription', 'dataKeys']
dataDescription = {}

for i, row in dd.iterrows():
    dataDescription[dd.dataKeys[i]] = dd.dataDecription[i]

def dataLookUp(item):
    try:
        print dataDescription[item]
    except:
        print item, "is not a valid data code"
            

def dataDescr():

    print "UC Berkeley Intro CS Student dataset"

    print "\nNotes"
    print "------"
    print "Data Set Characteristics:"

    print "\nNumber of Instances:{}".format(882)

    print "\nAttribute Information:"

    print "\nSelf reported attitudes about CS"
    print "- atcs_1 I like to use computer science to solve problems."
    print "- atcs_2 I can learn to understand computing concepts."
    print "- atcs_3 I can achieve good grades (C or better) in computing courses."
    print "- atcs_4 I do not like using computer science to solve problems."
    print "- atcs_5 I am confident that I can solve problems by using computation."
    print "- atcs_6 The challenge of solving problems using computer science appeals to me."
    print "- atcs_7 I am comfortable with learning computing concepts."
    print "- atcs_8 I am confident about my abilities with regards to computer science."
    print "- atcs_9 I do think I can learn to understand computing concepts."

    print "\nGendered belief about CS ability"
    print "- atcsgender_1 Women are less capable of success in CS than men."
    print "- atcsgender_2 Women are smarter than men."
    print "- atcsgender_3 Men have better math and science abilities than women."

    print "\nCareer driven beliefs about CS"
    print "- atcsjob_1 Knowledge of computing will allow me to secure a good job."
    print "- atcsjob_2 My career goals do not require that I learn computing skills."

    print "\nSelf reported attitudes about computational thinking"
    print "- atct_1 I am good at solving a problem by thinking about similar problems I have solved before."
    print "- atct_2 I have good research skills."
    print "- atct_3 I am good at using online search tools."
    print "- atct_4 I am persistent at solving puzzles or logic problems."
    print "- atct_5 I know how to write computer programs."
    print "- atct_6 I am good at building things."
    print "- atct_7 I am good at ignoring irrelevant details to solve a problem."
    print "- atct_8 I know how to write a computer program to solve a problem."

    print "\nSelf reported attitudes about CS class belonging"
    print "- blg_1 In this class, I feel I belong."
    print "- blg_2 In this class, I feel awkward and out of place."
    print "- blg_3 In this class, I feel like my ideas count."
    print "- blg_4 In this class, I feel like I matter."

    print "\nSelf reported beliefs about collegiality"
    print "- clet_1 I work well in teams."
    print "- clet_2 I think about the ethical, legal, and social implications of computing."
    print "- cltrcmp_1 I am comfortable interacting with peers from different backgrounds than my own (based on race, sexuality, income, and so on.)"
    print "- cltrcmp_2 I have good cultural competence, or the ability to interact effectively with people from diverse backgrounds."

    print "\nDemographics"
    print "- gender Could I please know your gender"
    print "- reason_class What is your reason for taking this class"
    print "- major What is your major?"

    print "\nCS mentors and role models"
    print "- mtr_1 Before I came to UC Berkeley, I knew people who have careers in Computer Science."
    print "- mtr_2 There are people with careers in Computer Science who look like me."
    print "- mtr_3 I have role models within the Computer Science field that look like me."

    print "\nPrior collegiate CS exposure"
    print "- prcs_1 Did you take a CS course in High School?"
    print "- prcs_2 Did you have any exposure to Computer Science before UC Berkeley?"
    print "- prcs_3 Did a family member introduce you to Computer Science?"
    print "- prcs_4 Did you have a close family member who is a Computer Scientist or is affiliated with computing industry?"
    print "- prcs_5 Did your high school offer AP CS?"

    print "\nMissing Attribute Values: None"

    print "\nCreator: Omoju Miller"




def process( CS61A_DATA, CS10SPRING_DATA_1, CS10SPRING_DATA_2  ):


    ## Lets go ahead and filter out missing data.
    ## If the consent value is "I disagree", then drop that row from the data set.

    CS61A_DATA = CS61A_DATA[CS61A_DATA.consent == 'I agree']
    CS10SPRING_DATA_1 = CS10SPRING_DATA_1[CS10SPRING_DATA_1.consent == 'I agree']
    CS10SPRING_DATA_2 = CS10SPRING_DATA_2[CS10SPRING_DATA_2.consent == 'I agree']

    ## Combine all the different data samples representing the two collections from CS10 and the one collection from 61a


    frames = [CS10SPRING_DATA_1, CS10SPRING_DATA_2, CS61A_DATA]
    student_data = pd.concat(frames, keys=['pre', 'post','61a'])
    columnsNotNeeded = ['timestamp', 'consent','name', 'name_1', 'name_2',
                    'morecs','snap_python','hiphop_d1','hiphop_d2','song_ct', 'major']
    student_data.drop(columnsNotNeeded, axis=1, inplace=True)


    return student_data

def preprocess():
    return process( CS61A_DATA, CS10SPRING_DATA_1, CS10SPRING_DATA_2 )

def load_model(model_filename):
    
    try:
        with open(model_filename, "r") as clf_infile:
            clf = pickle.load(clf_infile)
    except:
        print "Could not load model"
    return clf

def evaluate_chi(y, item):
    """
    y: a list of labels
    item: a feature
    
    Evaluates a chi squared score for the feature.
    """
    #contigency table of observed counts
    ct1 = pd.crosstab(y, item )

    #column percentages
    col_sum = ct1.sum(axis=0)
    col_percentage = ct1/col_sum 
    chi_squared_score, p_value, dof, expected = stats.chi2_contingency(ct1)
    
    return chi_squared_score, p_value, dof, expected

def expected_rates(C):
    """
    C: ndarray, shape (2,2) as given by scikit-learn confusion_matrix function
    

    Returns false positive and true positive rates.
    
    Modified Function courtesy Matt Hancock
    http://notmatthancock.github.io/2015/10/28/confusion-matrix.html
    """
 
    
    assert C.shape == (2,2), "Confusion matrix should be from binary classification only."
    
    # true negative, false positive, etc...
    tn = C[0,0]; fp = C[0,1]; fn = C[1,0]; tp = C[1,1];

    NP = fn+tp # Num positive examples
    NN = tn+fp # Num negative examples
    N  = NP+NN

    
    return dict(fpr=fp / (fp+tn+0.), 
                tpr=tp / (tp+fn+0.))
    


def show_confusion_matrix(C, model_name, filename, class_labels=['0','1']):
    """
    C: ndarray, shape (2,2) as given by scikit-learn confusion_matrix function
    class_labels: list of strings, default simply labels 0 and 1.
    filename: string to save file to

    Draws confusion matrix with associated metrics.
    
    Modified Function courtesy Matt Hancock
    http://notmatthancock.github.io/2015/10/28/confusion-matrix.html
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    assert C.shape == (2,2), "Confusion matrix should be from binary classification only."
    
    # true negative, false positive, etc...
    tn = C[0,0]; fp = C[0,1]; fn = C[1,0]; tp = C[1,1];

    NP = fn+tp # Num positive examples
    NN = tn+fp # Num negative examples
    N  = NP+NN

    fig = plt.figure(figsize=(7.5,5), dpi=300)
    ax  = fig.add_subplot(111)
    ax.imshow(C, interpolation='nearest', cmap=plt.cm.gist_heat)

    # Draw the grid boxes
    ax.set_xlim(-0.5,0.5)
    ax.set_ylim(0.5,-0.5)
    
    
    
    # Set xlabels
    ax.set_xlabel(model_name+'\nPredicted Label', fontsize=16)
    ax.set_xticks([0,1,1.5])
    ax.set_xticklabels(class_labels + [''])
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    # These coordinate might require some tinkering. Ditto for y, below.
    ax.xaxis.set_label_coords(0.5,1.2)

    # Set ylabels
    ax.set_ylabel('True Label', fontsize=16, rotation=90)
    ax.set_yticklabels(class_labels + [''],rotation=90)
    ax.set_yticks([0,1,1.5])
    ax.yaxis.set_label_coords(-0.09,0.65)


    # Fill in initial metrics: tp, tn, etc...
    ax.text(0,0,
            'True Neg: %d\n(Num Neg: %d)'%(tn,NN),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(0,1,
            'False Neg: %d'%fn,
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))

    ax.text(1,0,
            'False Pos: %d'%fp,
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))


    ax.text(1,1,
            'True Pos: %d\n(Num Pos: %d)'%(tp,NP),
            va='center',
            ha='center',
            bbox=dict(fc='w',boxstyle='round,pad=1'))


    # Fill in secondary metrics: accuracy, true pos rate, etc...
    ax.text(2.1,0,
            'False Pos Rate: %.2f%%'%((fp / (fp+tn+0.)) * 100),
            va='center',
            ha='center')

    ax.text(2.1,1,
            'True Pos Rate: %.2f%%'%((tp / (tp+fn+0.)) * 100),
            va='center',
            ha='center')


    plt.tight_layout()
    plt.savefig(filename, format='png', dpi=100)
    plt.close()
    
    
def create_feature_map(features, filename):
    """
    features: list of feature names for an xgboost tree
    filename: file name for the feature map file
    
    Creates a feature map for a xgboost model
    
    Courtesy Richard Xie
    http://www.gladwinanalytics.com/blog/an-information-gain-based-feature-ranking-function-for-xgboost
    """
    outfile = open(filename, 'w')
    i = 0
    for feat in features:
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close() 
    
def order_features_by_gains(bst, feature_map_file):
    """
    bst: xgboost model
    feature_map_file: feature map for a xgboost model
    
    Sorts features by the sum of gains in a descending order.
    
    Courtesy Richard Xie
    http://www.gladwinanalytics.com/blog/an-information-gain-based-feature-ranking-function-for-xgboost
    """
    str_dump = bst.get_dump(feature_map_file,with_stats=True)
    
    tree_arr = []
    for i_tree, tree in enumerate(str_dump):
        arr_lvls=tree.split('\n\t')
        a_tree = {}
        for lvl in arr_lvls:
            a_lvl ={}
            dum1 = lvl.split(',')
            if('leaf' in lvl):
                dum1[0].replace('\t','')
                dum10 = dum1[0].split(':')
                lvl_id = int(dum10[0])
                dum11 = dum10[1].split('leaf=')
                leaf = float(dum11[1])
                
                cover = float(dum1[1].replace('\n','').split('cover=')[1])
                a_lvl['lvl_id']=lvl_id
                a_lvl['leaf']=leaf
                a_lvl['cover']=cover
            else:
                dum10 = dum1[0].replace('\t','').replace('\n','')
                dum11 = dum10.split(':')
                lvl_id = int(dum11[0])
                dum12 = dum11[1].split('yes=')
                dum13 = dum12[0].replace('[','').replace(']','').split('<')
                feat_name = dum13[0]
                
                yes_to = int(dum12[1])
                no_to = int(dum1[1].split('no=')[1])
                missing = int(dum1[2].split('missing=')[1])
                gain = float(dum1[3].split('gain=')[1])
                cover = float(dum1[4].split('cover=')[1])            
                feat_thr = float(dum12[1])
                
                a_lvl['lvl_id']=lvl_id
                a_lvl['feat_name']=feat_name
                a_lvl['feat_thr'] = feat_thr
                a_lvl['yes_to'] = yes_to
                a_lvl['no_to']=no_to
                a_lvl['missing'] = missing
                a_lvl['gain']=gain
                a_lvl['cover']=cover
                
            a_tree[str(lvl_id)] = a_lvl
        tree_arr.append(a_tree)    
    feat_vocabulary = {}
    for tree in tree_arr:
        for lvl in tree:
            if('gain' in tree[lvl]):
                feat_data = feat_vocabulary.setdefault(tree[lvl]['feat_name'],{'gain':tree[lvl]['gain'],'cover':tree[lvl]['cover']})
                if(cmp(feat_data,{'gain':tree[lvl]['gain'],'cover':tree[lvl]['cover']})<>0):
                    try:
                        feat_vocabulary[tree[lvl]['feat_name']]['gain'] += tree[lvl]['gain']                    
                        feat_vocabulary[tree[lvl]['feat_name']]['cover'] += tree[lvl]['cover']
                    except:
                        feat_vocabulary[tree[lvl]['feat_name']]['gain'] = tree[lvl]['gain']                    
                        feat_vocabulary[tree[lvl]['feat_name']]['cover'] = tree[lvl]['cover']          
    
    sorted_feats = sorted(feat_vocabulary.items(),key=lambda k:k[1]['gain'], reverse=True)
    return sorted_feats
