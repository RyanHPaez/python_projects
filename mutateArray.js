function solution(n, a) {
    var result = [];
    for (var i= 0; i < n; i++) {
        var mutateValue = 0;
        if (a[i-1] !== undefined) {
            mutateValue += a[i-1];
        }
        if (a[i+1] !== undefined) {
            mutateValue += a[i+1];
        }
        mutateValue += a[i];
        result.push(mutateValue);
    }
    return result;
}