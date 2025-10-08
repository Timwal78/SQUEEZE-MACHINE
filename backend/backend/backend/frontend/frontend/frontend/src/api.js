export const getSignals = async () => fetch("/signals").then(r => r.json())
