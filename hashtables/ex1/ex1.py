cache = {}

def get_indices_of_item_weights(weights, length, limit):
    
    # build cache {weight: index}
    for k, v in enumerate(weights):
        cache[v] = k
    
    print(cache)

    # find indices of values that sum up to limit value
    for k, w in enumerate(weights):
        if (limit - w) in cache:
            if cache[limit-w] > k:
                return (cache[limit-w], k)
            else:
                return (k, cache[limit-w])
    
    return None
