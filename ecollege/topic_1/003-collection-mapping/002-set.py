# Sets
# the set class provides a mapping of unique immutable elements

empty_set = set()
print("empty set ->", empty_set)
alpha = set(("a", "b", "c", "d"))
print("alpha ->", alpha)
dup_list = ["c", "d", "c", "d", "e", "f"]
beta = set(dup_list)
print("beta ->", beta)
uniq_list = list(beta)
print("uniq_list ->", uniq_list)

gamma = alpha.union(beta)
print("gamma ->", gamma)
gamma = alpha | beta
print("gamma ->", gamma)

delta = alpha.intersection(beta)
print("delta ->", delta)
delta = alpha & beta
print(delta)

epsilon = alpha.difference(beta)
print("epsilon ->", epsilon)
epsilon = alpha - beta
print("epsilon ->", epsilon)

eta = alpha.symmetric_difference(beta)
print("eta ->", eta)
eta = alpha ^ beta
print("eta ->", eta)

print("epsilon.isdisjoint(delta) ->", epsilon.isdisjoint(delta))
print("epsilon.isdisjoint(eta) ->", epsilon.isdisjoint(eta))

print("epsilon.issubset(eta) ->", epsilon.issubset(eta))
print("epsilon.issubset(beta) ->", epsilon.issubset(beta))

print("eta.issuperset(epsilon) ->", eta.issuperset(epsilon))
print("beta.issuperset(epsilon) ->", beta.issuperset(epsilon))

feta = frozenset(eta)           # frozensets are immutable without updatingn methods
print("feta ->", feta)

zeta = set()
print("zeta ->", zeta)
zeta.add(3)
print("zeta ->", zeta)
zeta.add(4)
print("zeta ->", zeta)
