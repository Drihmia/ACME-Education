import Cookies from 'js-cookie'
import { useEffect, useState } from 'react'
import { User } from '../types'

export const useLogOut = () => {
    const logout = async () => {

        const currentUserCookie = Cookies.get('currentUser');
        const currentUser = currentUserCookie ? JSON.parse(currentUserCookie) : null;
        const accessToken = currentUser?.access_token;

        const headers: HeadersInit = {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
        }

        // Getting csrfToken from cookies and send them with fetch post request.
        const csrfToken = Cookies.get('csrf_access_token');
        if (csrfToken) {
            headers['X-CSRF-TOKEN'] = csrfToken;
        }

        // Revoking jwt token stored in access_token in cookies on server side.
        const response = await fetch(
            `${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/logout`,
                {
                method: 'POST',
                headers: headers,
                credentials: 'include', // ensure cookies are sent with the request
            });

        if (response.ok) {
            console.log('Logged out successfully');
        } else {
            console.error('Failed to log out');
        }

        Cookies.remove("currentUser")
    }
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
