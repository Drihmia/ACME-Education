export default function Layout({
    children, // will be a page or nested layout
  }: {
    children: React.ReactNode
  }) {
    return <>{children}</>
    // return <div className="w-full h-full">{children}</div>
  }
