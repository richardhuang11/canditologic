"""This is a project created for Jonnie Candito's Strength/Hypertrophy Linear Workout Program.
   This program keeps track of the user's physical attributes such as age, height, and weight.
   Moreover, it keeps track of the user's numbers for previous lifts, and helps the user adjust
   his/her progressions based on the set's RPE (Rate of Perceived Exertion). Main sets on
   strength days are performed with 80% of the user's ORM (One Rep Max), and hypertrophy days
   are performed with 70% of the user's ORM."""

import datetime

currentDT = datetime.datetime.now()

#print(currentDT.strftime("%Y-%m-%d"))

class Workout:
    """Keeps track of the user's information, including one rep maxes, workouts, height, and weight.
       Updates one rep maxes after each workout based on the workout's working sets."""

    orms1 = {}
    orms2 = {}
    optionals = {}
    working_sets1 = {}
    working_sets2 = {}
    working_sets3 = {}
    working_sets4 = {}
    atts = {}
    days = 1 #get current date for graph info
    strength = 0.80
    hypertrophy = 0.70

    #def __init__(self):

    def get_user_info(self): #add functionality for customized optional exercises
        """gets the user's initial one rep maxes and workout numbers for the optional supplementary
           exercises, as people do not perform one rep maxes on these exercises"""
        Workout.orms1['squat'] = [int(input("squat one rep max? "))]
        Workout.orms1['deadlift'] = [int(input("deadlift one rep max? "))]

        Workout.orms2['bench'] = [int(input("bench one rep max? "))]
        Workout.orms2['upper_back1'] = [int(input("upper back exercise one rep max? "))]
        Workout.orms2['shoulder'] = [int(input("shoulder exercise one rep max? "))]
        Workout.orms2['upper_back2'] = [int(input("second upper back exercise one rep max? "))]

        Workout.optionals['incline_press'] = [int(input("previous incline press 4 sets x 8 reps weight?"))]
        Workout.optionals['leg_ext'] = [int(input("previous leg extention 4 sets x 8-12 reps weight? "))]
        Workout.optionals['leg_press'] = [int(input("previous leg press 3 sets x 8-12 reps weight? "))]
        Workout.optionals['ham_curl'] = [int(input("previous hamstring curl 3 sets x 8-12 reps weight? "))]
        Workout.optionals['calf_raise'] = [int(input("previous calf raise 5 sets x 15 reps weight? "))]
        Workout.optionals['bi_curl'] = [int(input("previous bicep curl 3 sets x 10 reps weight? "))]
        Workout.optionals['tri_ext'] = [int(input("previous tricep extention 3 sets x 8-12 reps weight? "))]
        Workout.optionals['face_pull'] = [int(input("previous face pull 3 sets x 8-12 reps weight? "))]


    def get_init_info(self):
        """gets the user's initial info: age, weight, and height"""
        Workout.atts['age'] = [int(input("What is your age? "))]
        Workout.atts['weight'] = [int(input("What is your weight? "))]
        Workout.atts['height'] = [raw_input("What is your height? ")]

    #Make this the __init__??
    def init_working_sets(self): #add functionality for customized optional exercises
        """calculates the user's initial numbers for his/her working sets based on his/her one rep maxes."""
        if Workout.days%4 == 1:
            print("Your workout today is: Strength Lower ")
            for lift in Workout.orms1:
                if 'deadlift' in lift:
                    print(lift, Workout.orms1[lift] * Workout.strength,' 2 sets x 6 reps')
                else:
                    print(lift, Workout.orms1[lift] * Workout.strength,' 3 sets x 6 reps')
            print('Leg Extensions ', Workout.optionals['leg_ext'],' 3 sets x 8-12 reps')
            print('Hamstring Curls ', Workout.optionals['ham_curl'],' 3 sets x 8-12 reps')
                Workout.working_sets1[lift] = Workout.orms1[lift] * Workout.strength
        elif Workout.days%4 == 2:
            print("Your workout today is: Strength Upper ") #specify which orm
            for i in Workout.orms2:
                if 'shoulder' or 'upper_back2' in lift:
                    print(lift,Workout.orms2[lift] * Workout.strength,' 1 set x 6 reps')
                else:
                    print(lift,Workout.orms2[lift] * Workout.strength,' 3 sets x 6 reps')
            print('Bicep Curls ', Workout.optionals['bi_curl'],' 3 sets x 8-12 reps')
            print('Tricep Extensions ', Workout.optionals['tri_ext'],' 3 sets x 8-12 reps')
                Workout.working_sets2[lift] = Workout.orms2[lift] * Workout.strength
        elif Workout.days%4 == 3:
            print("Your workout today is: Hypertrophy Lower ")
            for lift in Workout.orms1:
                if 'deadlift' in lift:
                    print(lift, Workout.orms1[lift] * Workout.strength, '3 sets x 8 reps')
                else:
                    print(lift, Workout.orms1[lift] * Workout.strength, '5 sets x 8 reps')
            print('Hamstring Curl ', Workout.optionals['ham_curl'],' 3 sets x 12 reps')
            print('Calf Raise ', Workout.optionals['calf_raise'],' 5 sets x 15 reps')
            print('Leg Press ', Workout.optionals['leg_press'], '4 sets x 8-12 reps')
            print('Leg Extensions ', Workout.optionals['leg_ext'],' 4 sets x 8-12 reps')
                Workout.working_sets3[lift] = Workout.orms[lift] * Workout.strength
        elif Workout.days%4 == 0:
            print("Your workout today is: Hypertrophy Upper ") 
            for lift in Workout.orms:
                if 'shoulder' in lift:
                    print(lift, Workout.orms2[lift] * Workout.strength,' 3 sets x 10 reps')
                else:
                    print(lift, Workout.orms2[lift] * Workout.strength,' 4 sets x 8 reps')
            print('Incline Press ', Workout.optionals['incline_press'],' 4 sets x 8 reps')
            print('Bicep Curl ', Workout.optionals['bi_curl'],' 3 sets x 10 reps')
            print('Tricep Extensions ', Workout.optionals['tri_ext'],' 4 sets x 8-12 reps')
            print('Face Pulls ', Workout.optionals['face_pull'],' 4 sets x 8-12 reps')
                Workout.working_sets4[lift] = Workout.orms[lift] * Workout.strength

class update_info(Workout):
    """updates the user's age, weight, and height"""
    def update_weight(self):
        Workout.atts['weight'].append(int(input("What is your weight? ")))
        
    def update_age(self):
        Workout.atts['age'].append(int(input("What is your age? ")))

    def update_height(self):
        Workout.atts['height'].append(int(input("What is your height? ")))

class pre_workout(Workout):
    """Includes methods performed before the user's workout such as generating the workout
       for the day."""

    # def sets_generator(self,bodypart,focus):
    #     if i ==
    #     for i in self.orms:
    #         print(i,self.orms[i] * type)
    #         self.working_sets[i] = self.orms[i] * type

    def get_working_sets(self):
        if Workout.days%4 == 1:
            print("Your workout today is: Strength Lower ")
            # self.sets_generator(self.strength)
            for lift in Workout.working_sets1:
                if 'deadlift' in lift:
                    print(lift,Workout.working_sets1[lift][len(Workout.working_sets1[lift]) - 1],' 2 sets x 6 reps')
                else:
                    print(lift,Workout.working_sets1[lift][len(Workout.working_sets1[lift]) - 1],' 3 sets x 6 reps')
            print('Leg Extensions ', Workout.optionals['leg_ext'][len(Workout.working_sets1['leg_ext'])-1],' 3 sets x 8-12 reps')
            print('Hamstring Curls ', Workout.optionals['ham_curl'][len(Workout.working_sets1['ham_curl'])-1],' 3 sets x 8-12 reps')
        elif Workout.days%4 == 2:
            print("Your workout today is: Strength Upper ") #specify which orm
            for lift in Workout.working_sets2:
                if 'shoulder' or 'upper_back2' in lift:
                    print(lift,Workout.orms2[lift] * Workout.strength,' 1 set x 6 reps')
                else:
                    print(lift,Workout.orms2[lift] * Workout.strength,' 3 sets x 6 reps')
            print('Bicep Curls ', Workout.optionals['bi_curl'],' 3 sets x 8-12 reps')
            print('Tricep Extensions ', Workout.optionals['tri_ext'],' 3 sets x 8-12 reps')
                Workout.working_sets2[lift] = Workout.orms2[lift] * Workout.strength
        elif Workout.days%4 == 3:
            print("Your workout today is: Hypertrophy Lower ")
            for lift in Workout.working_sets3:
                if 'deadlift' in lift:
                    print(lift, Workout.orms1[lift] * Workout.strength, '3 sets x 8 reps')
                else:
                    print(lift, Workout.orms1[lift] * Workout.strength, '5 sets x 8 reps')
            print('Hamstring Curl ', Workout.optionals['ham_curl'],' 3 sets x 12 reps')
            print('Calf Raise ', Workout.optionals['calf_raise'],' 5 sets x 15 reps')
            print('Leg Press ', Workout.optionals['leg_press'], '4 sets x 8-12 reps')
            print('Leg Extensions ', Workout.optionals['leg_ext'],' 4 sets x 8-12 reps')
                Workout.working_sets3[lift] = Workout.orms[lift] * Workout.strength
        elif Workout.days%4 == 0:
            print("Your workout today is: Hypertrophy Upper ") 
            for lift in Workout.working_sets4:
                if 'shoulder' in lift:
                    print(lift, Workout.orms2[lift] * Workout.strength,' 3 sets x 10 reps')
                else:
                    print(lift, Workout.orms2[lift] * Workout.strength,' 4 sets x 8 reps')
            print('Incline Press ', Workout.optionals['incline_press'],' 4 sets x 8 reps')
            print('Bicep Curl ', Workout.optionals['bi_curl'],' 3 sets x 10 reps')
            print('Tricep Extensions ', Workout.optionals['tri_ext'],' 4 sets x 8-12 reps')
            print('Face Pulls ', Workout.optionals['face_pull'],' 4 sets x 8-12 reps')
                Workout.working_sets4[lift] = Workout.orms[lift] * Workout.strength


        if Workout.days%4 == 1:
            for lift in Workout.working_sets1:
                exercise = Workout.working_sets1
                print(lift,exercise[len(exercise[lift]) - 1])
        if Workout.days%4 == 2:
            for lift in Workout.working_sets2:
                print(lift,Workout.working_sets2[len(Workout.working_sets2[lift]) - 1])
        if Workout.days%4 == 3:
            for lift in Workout.working_sets3:
                print(lift,Workout.working_sets3[len(Workout.working_sets3[lift]) - 1])
        if Workout.days%4 == 0:
            for lift in Workout.working_sets4:
                print(lift,Workout.working_sets4[len(Workout.working_sets4[lift]) - 1])

class post_workout(Workout):
    """Includes methods performed after the user's workout such as determining which exercises
       were fully completed and how to increment the working set for the next workout."""
    def completed_set(self, lift_name):
        increment = 5
        exercise = None
        user_input = raw_input("Did you complete this" + lift_name + " set? ")
        if user_input == 'n':
            print("Better luck next time!")
        elif user_input == 'y':
            rpe = self.get_rpe()
            if 'bench' or 'incline_press' or 'squat' or 'dl' or 'upper_back' in lift_name and rpe <= 5:     
               increment = 10
            if Workout.days%4 == 1:
                exercise = Workout.working_sets1[lift_name]
                self.do_increment(exercise, increment)
            elif Workout.days%4 == 2:
                exercise = Workout.working_sets2[lift_name]
                self.do_increment(exercise, increment)
            elif Workout.days%4 == 3:
                exercise = Workout.working_sets3[lift_name]
                self.do_increment(exercise, increment)
            elif Workout.days%4 == 0:
                exercise = Workout.working_sets4[lift_name]
                self.do_increment(exercise, increment)
        else:
            print "Invalid response: please enter y or n."

    def do_increment(self, exc, inc):
        workout.append(workout[len(workout)-1] + increment)

    def get_rpe(self):
        return int(input("RPE for this set? "))