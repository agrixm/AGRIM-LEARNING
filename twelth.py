#f strings

# l="my name is {0} and i am {1} years old"
# name="Agrim"
# age=20
# print(l.format(name,age))


# l="my name is {name} and i am {age} years old"
# name="Agrim"
# age=20.099 
# print(f"my name is {age:.2f} and i am {age:.2f} years old")
# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")
# print(f"{2 * 30}")


#Docstring
# def square(n):
#   '''Takes in a number n, returns the square of n'''
#   print(n**2)
# square(5)
# print(square.__doc__)
# def add(num1, num2):
#     """
#     Add up two integer numbers.
#     This function simply wraps the ``+`` operator, and does not
#     do anything interesting, except for illustrating what
#     the docstring of a very simple function looks like.
#     Parameters
#     ----------
#     num1 : int
#         First number to add.
#     num2 : int
#         Second number to add.
#     Returns
#     -------
#     int
#         The sum of ``num1`` and ``num2``.
#     See Also
#     --------
#     subtract : Subtract one integer from another.
#     Examples
#     --------
#     >>> add(2, 2)
#     4
#     >>> add(25, 0)
#     25
#     >>> add(10, -10)
#     0
#     """
    
#     print(num1 + num2)
# add(5, 5)
# print(add.__doc__)

#Recusrion
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(9))
    
