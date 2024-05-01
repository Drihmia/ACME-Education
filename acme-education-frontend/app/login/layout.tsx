export default function LoginLayout({
    children, // will be a page or nested layout
  }: {
    children: React.ReactNode
  }) {
    return <main className="w-full h-[calc(100vh-64px)] md:h-[calc(100vh-80px)] grid place-items-center bg-sky-50">{children}</main>
  }
