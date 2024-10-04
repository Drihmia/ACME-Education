import { NextRequest, NextResponse } from "next/server";

const protectedRoutes = '/dashboard'
// const teacherOnlyRoutes = ['/dashboard/lessons/add', '/dashboard/lessons/edit']
const authRoutes = ['/', '/login', '/signup']

const checkjwt = async (request: NextRequest) => {
    const token = request.cookies.get('access_token')?.value;
    // console.log(token);

    if (!token) {
        return false;
    }

    try {
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/checkjwt`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Cookie': `access_token=${token}`,
            },
        });

        const data = await res.json();

        // Check if the token has expired based on the jwtIsValid or response
        if (!data.jwtIsValid || !res.ok) {
            return false;
        }

        return true;

    } catch (error) {
        return false;
    }
};

export async function middleware(request: NextRequest) {
const currentUser = request.cookies.get("currentUser")?.value

const jwtIsValid = await checkjwt(request)

// currentUser Gives info about the manual logout by the user, if currentUser is not found in cookies
// means that the user has manually logged out, no need the check the JWT token.
if (request.nextUrl.pathname.startsWith(protectedRoutes) && ((!currentUser) || (!jwtIsValid))) {
        request.cookies.delete("currentUser")
        request.cookies.delete("access_token")
        const response = NextResponse.redirect(new URL("/login", request.url))
        response.cookies.delete("currentUser")
        response.cookies.delete("access_token")


        return response
    }

    if (authRoutes.includes(request.nextUrl.pathname) && (currentUser)) {
        return NextResponse.redirect(new URL("/dashboard", request.url))
    }
}
