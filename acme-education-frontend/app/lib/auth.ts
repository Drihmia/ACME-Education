import Cookies from 'js-cookie'
import { useCallback, useEffect, useState } from 'react'
import { User } from '../types'

export const useLogOut = () => {
    const logout = () => Cookies.remove("currentUser")
    return logout
}

export const useCurrentUser = () => {
    const [user, setUser] = useState<User | null>(null)

    useEffect(() => {
        const currentUser = Cookies.get("currentUser")

        if (currentUser) setUser(JSON.parse(currentUser))
    }, [])

    return user
}
