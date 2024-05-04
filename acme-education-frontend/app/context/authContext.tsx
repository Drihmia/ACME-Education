"use client"

import Cookies from 'js-cookie'
import { User, UserContext } from "@/app/types";
import { createContext, useContext, useEffect, useState } from "react";


export const authUserContext = createContext<UserContext | null>(null)

export function AuthUserProvider({children}: { children: React.ReactNode }) {
    const [user, setUser] = useState<User | null>(null)

    const updateUser = () => {
        const currentUser = Cookies.get("currentUser")
        if (currentUser) {
            setUser(JSON.parse(currentUser))
        } else {
            setUser(null)
        }
    }

    useEffect(() => {
        const currentUser = Cookies.get("currentUser")

        if (currentUser) setUser(JSON.parse(currentUser))
    }, [])

    return <authUserContext.Provider value={{user, updateUser}}>{children}</authUserContext.Provider>
}

//custom hook to use the authUserContext and access user and loading
export const useAuth = () => useContext(authUserContext)
