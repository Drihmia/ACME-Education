export default function LoginLayout({
    children, // will be a page or nested layout
  }: {
    children: React.ReactNode
  }) {
    return <main className="w-full min-h-[calc(100vh-64px)] md:min-h-[calc(100vh-80px)] grid place-items-center p-4 md:p-8 lg:p-16 bg-sky-50">{children}</main>
  }
