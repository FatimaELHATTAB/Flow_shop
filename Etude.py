import solve_problem
import numpy as np

list_job = [20]
list_machine = [5,10]
list_probabilite = [0,0.2,0.5,0.8,1]
list_population =[20,30,40]
list_generation = [20,40,60]

def AG_study():
    #on parcours tous les problemes
    for i in range(1,10):
        #on parcours tous les tailles d'instances
        for j in list_machine:
            for k in list_job:
                print("probleme ", i, j, k, "  : \n")
                makespan_list = []
                #toutes les combinaisons possibles de probabilites et de taille population et taille generation
                for p in list_probabilite:
                    for o in list_population:
                        for g in list_generation:
                            sequence, makespan = solve_problem.solve_benchmark_problem(i,k,j,o,g,p)
                            makespan_list.append(makespan)
                print(makespan_list)
                print(np.min(makespan_list))





def test_AG(instance, job, machine):
    print("probleme ", instance, job, machine, "  : \n")
    makespan_list = []
    # toutes les combinaisons possibles de probabilites et de taille population et taille generation
    for p in list_probabilite:
        for o in list_population:
            for g in list_generation:
                sequence, makespan = solve_problem.solve_benchmark_problem(instance, job, machine, o, g, p)
                makespan_list.append(makespan)
    print(makespan_list)
    print(np.min(makespan_list))
