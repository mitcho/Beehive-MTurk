#!/usr/bin/python2.7

import csv
import sys
#TrialName
#PreempAllowed
#NumRows
#NumShapes
#[Shape Color Radius Position]
#TimeSpentOnFrame
#UserAnswer1
#CorrectAnswer1
#IsCorrect1
#UserAnswer2
#CorrectAnswer2
#IsCorrect2
#Frame
#TimeToAnswer1FromBegin
#TimeToStart2
#TimeToFinish2;

if len(sys.argv) < 3:
    print 'Format: python mt2mlpy [csv from MTurk] [output csv]'
    quit()
    
reader = csv.DictReader(open(sys.argv[1],'rb'))
writer= 0;

for row in reader:
    data = {}
    data['Experiment'] = row['Answer.Experiment']
    data['UserComment'] = row['Answer.comments']
    data['WorkerID'] = row['WorkerId']
    
    trial_names = row['Answer.Trial names:'].split(' ')
    for trial_name in trial_names:
        data['TrialName'] = trial_name
        num_frames = int(row['Answer.' + trial_name + '.num_frames']);
        data['NumFrames'] = num_frames
        num_rows = int(row['Answer.' + trial_name + '.num_rows']);
        data['NumRows'] = num_rows
        num_shapes = int(row['Answer.' + trial_name + '.num_shapes']);
        data['NumShapes'] = num_shapes
        preemp_allowed = row['Answer.' + trial_name + '.preemp_allowed'];
        data['PreempAllowed'] = preemp_allowed

        usr_answer1 = row['Answer.' + trial_name + '.usr_answer1'];
        data['UserAnswer1'] = usr_answer1
        correct_answer1 = row['Answer.' + trial_name + '.correct_answer1'];
        data['CorrectAnswer1'] = correct_answer1
        is_correct1 = row['Answer.' + trial_name + '.is_correct1'];
        data['IsCorrect1'] = is_correct1
        
        usr_answer2 = row['Answer.' + trial_name + '.usr_answer2'];
        data['UserAnswer2'] = usr_answer2
        correct_answer2 = row['Answer.' + trial_name + '.correct_answer2'];
        data['CorrectAnswer2'] = correct_answer2
        is_correct2 = row['Answer.' + trial_name + '.is_correct2'];
        data['IsCorrect2'] = is_correct2
        
        time_start_to_answer = row['Answer.' + trial_name + '.time_start_to_answer'];
        data['TimeToAnswer1FromBegin'] = time_start_to_answer/1000.0
        
        for j in range(1,num_frames+1):
            i = str(j)
            shapes = row['Answer.' + trial_name + '.' + i + '.shapes'];
            data['[Shape Color Radius Position]'] = shapes
            data['Frame'] = i
            time_spent = row['Answer.' + trial_name + '.' + i + '.time_spent'];
            data['TimeSpentOnFrame'] = time_spent/1000.0
            if writer == 0:
                writer = csv.DictWriter(open(sys.argv[2],'w'),sorted(data))
                writer.writeheader()
            writer.writerow(data)
            
    