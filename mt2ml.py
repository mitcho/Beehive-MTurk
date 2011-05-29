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
    for i in range(len(trial_names)):
        trial_name = trial_names[i]
        data['TrialName'] = trial_name
        num_frames = int(row['Answer.' + str(i) + '.num_frames']);
        data['NumFrames'] = num_frames
        num_rows = int(row['Answer.' + str(i) + '.num_rows']);
        data['NumRows'] = num_rows
        num_shapes = int(row['Answer.' + str(i) + '.num_shapes']);
        data['NumShapes'] = num_shapes
        preemp_allowed = row['Answer.' + str(i) + '.preemp_allowed'];
        data['PreempAllowed'] = preemp_allowed

        frame_answered = row['Answer.' + str(i) + '.end_frame'];
        data['FrameAnswered'] = frame_answered

        usr_answer1 = row['Answer.' + str(i) + '.usr_answer1'];
        data['UserAnswer1'] = usr_answer1
        correct_answer1 = row['Answer.' + str(i) + '.correct_answer1'];
        data['CorrectAnswer1'] = correct_answer1
        is_correct1 = row['Answer.' + str(i) + '.is_correct1'];
        data['IsCorrect1'] = is_correct1
        
        usr_answer2 = row['Answer.' + str(i) + '.usr_answer2'];
        data['UserAnswer2'] = usr_answer2
        correct_answer2 = row['Answer.' + str(i) + '.correct_answer2'];
        data['CorrectAnswer2'] = correct_answer2
        is_correct2 = row['Answer.' + str(i) + '.is_correct2'];
        data['IsCorrect2'] = is_correct2
        
        time_start_to_answer = float(row['Answer.' + str(i) + '.time_start_to_answer']);
        data['TimeToAnswer1FromBegin'] = time_start_to_answer/1000.0
        
        for j in range(1,num_frames+1):
            k = str(j)
            shapes = row['Answer.' + str(i) + '.' + k + '.shapes'];
            data['[Shape Color Radius Position]'] = shapes
            data['Frame'] = k
            time_spent = float(row['Answer.' + str(i) + '.' + k + '.time_spent']);
            data['TimeSpentOnFrame'] = time_spent/1000.0
            if writer == 0:
                writer = csv.DictWriter(open(sys.argv[2],'w'),sorted(data))
                writer.writeheader()
            writer.writerow(data)
            
    