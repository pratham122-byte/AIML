# Predicate Logic Fact Checker

# Store predicate facts
facts = {
    "parent": [("John", "Mary"), ("Alice", "Bob")],
    "brother": [("Tom", "Jerry"), ("Bob", "Sam")],
    "teacher": [("Smith", "Alice"), ("Brown", "John")]
}

# User query
query = input("Enter a query (example: parent(John, Mary)): ")

# Parse the query
predicate = query[:query.index("(")]
args = query[query.index("(")+1 : query.index(")")].split(",")

arg1 = args[0].strip()
arg2 = args[1].strip()

# Check if fact exists
if predicate in facts and (arg1, arg2) in facts[predicate]:
    print("Fact exists")
else:
    print("Fact does NOT exist")