import { useEffect, useRef } from "react"

export const useOutsideClick =(callback?: () => void) => {


    const ref = useRef<HTMLDivElement | null>(null)

    useEffect(() => {

        const handleClick = (event: MouseEvent): void => {
            if (ref.current && !ref.current.contains(event.target as Node)) {
                if (callback) {
                    callback()
                }
            }
        }

        if (typeof document !== 'undefined') {
            document.addEventListener('click', handleClick, true);
            return () => {
                document.removeEventListener('click', handleClick, true);
            };
        }


    }, [callback])

    return ref
}
