import { NextRequest, NextResponse } from "next/server";

const protectedRoutes = '/dashboard'
// const teacherOnlyRoutes = ['/dashboard/lessons/add', '/dashboard/lessons/edit']
const authRoutes = ['/', '/login', '/signup']


export function middleware(request: NextRequest) {
    const currentUser = request.cookies.get("currentUser")?.value

    if (request.nextUrl.pathname.startsWith(protectedRoutes) && (!currentUser)) {
        request.cookies.delete("currentUser")
        request.cookies.delete("access_token")
        const response = NextResponse.redirect(new URL("/login", request.url))
        response.cookies.delete("currentUser")
        response.cookies.delete("access_token")

        return response
    }

    if (authRoutes.includes(request.nextUrl.pathname) && currentUser) {
        return NextResponse.redirect(new URL("/dashboard", request.url))
    }
}
