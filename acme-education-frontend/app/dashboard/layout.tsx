import { SideNav } from "../ui/dashboard/sidenav";

 
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <main className="flex h-[80.4vh] flex-col md:flex-row md:overflow-hidden">
      <div className="w-full flex-none md:w-64">
        <SideNav />
      </div>
      <div className="flex-grow p-4 md:overflow-y-auto md:p-8">{children}</div>
    </main>
  );
}