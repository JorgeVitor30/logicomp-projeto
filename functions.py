"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """


    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula):
    """Returns the set of all atoms occurring in a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for atom in atoms(my_formula):
        print(atom)

    This piece of code above prints: p, s
    (Note that there is no repetition of p)
    """
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def number_of_atoms(formula):
    """Returns the number of atoms occurring in a formula.
    For instance,
    number_of_atoms(Implies(Atom('q'), And(Atom('p'), Atom('q'))))

    must return 3 (Observe that this function counts the repetitions of atoms)
    """
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def number_of_connectives(formula):
    """Returns the number of connectives occurring in a formula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_literal(formula):
    """Returns True if formula is a literal. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def substitution(formula, old_subformula, new_subformula):
    """Returns a new formula obtained by replacing all occurrences
    of old_subformula in the input formula by new_subformula."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_clause(formula):
    """Returns True if formula is a clause. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def turn_common_inscriptions_pair_minicourses_to_propositional_logic(cx, cy, slots):
    firstCourseInFirstSlot = Atom(f"x_{cx}_1")
    secondCourseInFirstSlot = Atom(f"x_{cy}_1")
    formula = Not(And(firstCourseInFirstSlot, secondCourseInFirstSlot))

    for slot in range(2, slots+1):
        formula = And(formula, Not(And(Atom(f"x_{cx}_{slot}"), Atom(f"x_{cy}_{slot}"))))
    

    return formula


def at_least_in_one_slot(cx, slots):
    firstCourseInFirstSlot = Atom(f"x_{cx}_1")
    formula = firstCourseInFirstSlot

    for slot in range(2, slots+1):
        formula = Or(formula, Atom(f"x_{cx}_{slot}"))

    return formula

def max_in_one_slot(cx, slots):

    for x in range(1, slots + 1):
        for y in range(x + 1, slots + 1):
            not_in_two_slots = Not(And(Atom(f"x_{cx}_{x}"),Atom(f"x_{cx}_{y}")))
            print(not_in_two_slots)

def implication_free(formula):
    if (isinstance(formula, Implies) or isinstance(formula, Or) or isinstance(formula, And)):
        left = implication_free(formula.left)
        right = implication_free(formula.right)
        
        if (isinstance(formula, Implies)):
            return (Or(Not(left), right))
        
        if (isinstance(formula, Or)):
            return Or(left, right)
        
        if (isinstance(formula, And)):
            return And(left, right)
        
    if (isinstance(formula, Not)):
        inner = implication_free(formula.inner)
        return Not(inner)
    
    if (isinstance(formula, Atom)):
        return formula
    return formula

def negation_normal_form(formula):    
    if (isinstance(formula, Not) and isinstance(formula.inner, Not)):
        removed_double_negation_formula = formula.inner.inner
        return negation_normal_form(removed_double_negation_formula)
    
    if (isinstance(formula, Or)):
            return Or(negation_normal_form(formula.left), negation_normal_form(formula.right))
        
    if (isinstance(formula, And)):
            return And(negation_normal_form(formula.left), negation_normal_form(formula.right))
        
    if (isinstance(formula, Not)):
        inner_formula = formula.inner

        if (isinstance(inner_formula, Or)):
                return And(negation_normal_form(Not((inner_formula.left))), negation_normal_form(Not(inner_formula.right)))
            
        if (isinstance(inner_formula, And)):
                return Or(negation_normal_form(Not(inner_formula.left)), negation_normal_form(Not(inner_formula.right)))
    
    if (isinstance(formula, Atom) or (isinstance(formula, Not) and isinstance(formula.inner, Atom))):
        return formula
    
    return formula

def distributive(formula):
    if (isinstance(formula, And)):
        return And(distributive(formula.left), distributive(formula.right))
    
    if (isinstance(formula, Or)):
        left = distributive(formula.left)
        right = distributive(formula.right)
        if (isinstance(left, And)):
            return And(distributive(Or(left.left, right)), distributive(Or(left.right, right)))
        
        if (isinstance(right, And)):
            return And(distributive(Or(left, right.left)), distributive(Or(left, right.right)))
        
    if (isinstance(formula, Atom) or (isinstance(formula, Not) and isinstance(formula.inner, Atom))):
        return formula
    
    return formula

def cnf(formula):
    implication_free_formula = implication_free(formula)
    nnf_formula = negation_normal_form(implication_free_formula)
    cnf_formula = distributive(nnf_formula)

    return cnf_formula