import { NextRequest, NextResponse } from "next/server";

const protectedRoutes = ['/dashboard']
const authRoutes = ['/', '/login', '/signup']


export function middleware(request: NextRequest) {
    const currentUser = request.cookies.get("currentUser")?.value

    if (protectedRoutes.includes(request.nextUrl.pathname) && (!currentUser)) {
        request.cookies.delete("currentUser")
        const response = NextResponse.redirect(new URL("/login", request.url))
        response.cookies.delete("currentUser")

        return response
    }

    if (authRoutes.includes(request.nextUrl.pathname) && currentUser) {
        return NextResponse.redirect(new URL("/dashboard", request.url))
    }
}
