from utils import *
'''
The arpanet according to Fig 2.3 p 23
'''
F23 = toGraph({
  'MIT': ['LNC', 'BBN', 'UTAH'],
  'LNC': ['MIT', 'CASE'],
  'CARN': ['CASE', 'HARV'],
  'HARV': ['BBN', 'CARN'], 
  'BBN': ['MIT', 'HARV', 'RAND'],
  'RAND': ['BBN', 'SDC', 'UCLA'],
  'UCLA': ['RAND', 'STAN', 'UCSB'],
  'SDC': ['UTAH', 'RAND'],
  'STAN': ['SRI', 'UCLA'],
  'UCSB': ['UCLA', 'SRI'],
  'SRI': ['UCSB', 'UCLA', 'STAN'],
  'UTAH': ['SRI', 'SDC', 'MIT'],
})

'''
Gate keeper Graph
'''
F214 = toGraph({
  'D': ['B', 'C'],
  'C': ['D', 'A'],
  'B': ['D', 'A'],
  'A': ['B', 'C', 'E', 'F', 'D'],
  'E': ['A', 'F'],
  'F': ['A', 'E']
})

F31 = toGraph({
       'G': ['B'],
       'B': ['G', 'F', 'A'],
       'F': ['B', 'E'],
       'E': ['F', 'A'],
       'A': ['B', 'E', 'C', 'D'],
       'C': ['A', 'D'],
       'D': ['A', 'C']
})

F33 = fromDot('''strict graph A {
    C -- A;
    C -- E;
    C -- D;
    D -- A;
    E -- D;
    E -- A;
    A -- B;
    B -- F;
    B -- G;
    B -- H;
    F -- G;
    F -- H;
    G -- H;
}   
''')

F34 = fromDot('''strict graph A { 
    C -- F;
    A -- F;
    F -- J;
    J -- G;
    F -- G;
    G -- K;
    G -- H;
    K -- H;
    H -- B;
    H -- R;
    C -- A;
    C -- E;
    C -- D;
    D -- A;
    E -- D;
    E -- A;
    A -- B;
    B -- R;
    B -- P;
    B -- O;
    R -- P;
    R -- O;
    P -- O;
}   
''')

F35 = fromDot('''strict graph A { 
    C -- F [weight=.5];
    A -- F [weight=.5];
    F -- J [weight=1];
    J -- G [weight=1];
    F -- G [weight=1];
    G -- K [weight=.5];
    G -- H [weight=.5];
    K -- H [weight=1];
    H -- B [weight=.5];
    H -- R [weight=.5];
    C -- A [weight=1];
    C -- E [weight=1];
    C -- D [weight=1];
    D -- A [weight=1];
    E -- D [weight=.5];
    E -- A [weight=1];
    A -- B [weight=.5];
    B -- R [weight=1];
    B -- P [weight=1];
    B -- O [weight=1];
    R -- P [weight=1];
    R -- O [weight=.5];
    P -- O [weight=1];
}   
''')

F42 = fromDot('''
strict graph F42 {
   node [fillcolor=green, style=filled];
   A; B; C; D; E; F;
   G[fillcolor=white]; 
   H[fillcolor=white]; 
   I[fillcolor=white];
   A -- B; 
   A -- C;
   A -- D;
   A -- E;
   B -- C;
   C -- D;
   D -- E;
   D -- F;
   E -- F;
   F -- G;
   G -- I;
   G -- H;
   H -- I;
   B -- I;
   B -- H;
   D -- I;
}
''')
