import { fetcher } from "@/app/lib/fetch";
import { User } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import useSWR from "swr";

export const Profile = ({ user }: { user: User }) => {
  const { data: teacherData, error } = useSWR(
    `http://127.0.0.1:5000/api/v1/teachers/${user.user_id}`,
    fetcher, { suspense: true}
  );

  if (error) return <p>There was an error.</p>


  return (
    <div className="w-full grid gap-4">
      <h1 className={`text-2xl md:text-3xl font-bold`}>
        My Profile <span className="block text-lg">ID: {teacherData.id}</span>
      </h1>
      <div className="w-full grid md:grid-cols-2 gap-4 md:gap-8">
        <div className="w-full flex items-center justify-center">
          <Icon fontSize={256} icon="lets-icons:user-box-light" />
        </div>
        <div className="w-full flex flex-col gap-2">
          <h2 className="text-xl md:text-2xl lg:text-3xl font-semibold">
            Personal Info
          </h2>
          <ul className="w-full flex flex-col gap-1">
            <li className="text-lg md:text-xl font-medium">
              First Name:{" "}
              <span className="font-normal">{teacherData.first_name}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Last Name:{" "}
              <span className="font-normal">{teacherData.last_name}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Email: <span className="font-normal">{teacherData.email}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Institution:{" "}
              <span className="font-normal">{teacherData.institution}</span>
            </li>
          </ul>
          <button className="w-16 self-end flex items-center gap-1 py-1 px-2 mt-4 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize">
            <Icon icon="mage:edit" /> Edit
          </button>
        </div>
      </div>
    </div>
  );
};
