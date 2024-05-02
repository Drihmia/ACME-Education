export const fetcher = (args: string) => fetch(args).then(res => res.json())
