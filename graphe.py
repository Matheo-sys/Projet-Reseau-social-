Son = ["Aurora", "Ilona", "Olavi", "Tapio"]

Mat = [
    [ 0 , 0 , 1 , 1 ],
    [ 0 , 0 , 0 , 0 ],
    [ 0 , 0 , 0 , 1 ],
    [ 0 , 0 , 1 , 0 ]
]

Adj = {
"Aurora" : ["Olavi", "Tapio"],
"Ilona" : [ ],
"Olavi" : [ "Tapio" ],
"Tapio" : [ "Olavi" ]
}