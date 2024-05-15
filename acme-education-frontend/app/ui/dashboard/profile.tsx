import { fetcher } from "@/app/lib/fetch";
import { User } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import useSWR, { mutate } from "swr";

export const Profile = ({ user, openModal }: { user: User, openModal: (item: any) => void }) => {
  const { data: profileData, error } = useSWR(
    `http://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/${user.class.toLowerCase()}s/${user.user_id}`,
    fetcher, { suspense: true}
  );
  
  const { data: subjectsList } = useSWR(
    `http://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${user.user_id}/subjects`,
    fetcher, { suspense: true}
  );

  mutate(`http://${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${user.user_id}/subjects`)

  // console.log(subjectsList);
  
  
  if (error) return <p>There was an error.</p>

  return (
    <div className="w-full h-full flex flex-col gap-4 md:gap-8">
      <h1 className={`text-2xl md:text-3xl font-bold`}>
        My Profile <span className="block text-lg">ID: {profileData.id}</span>
      </h1>
      <div className="w-full h-full grid md:grid-cols-[1fr_3fr] gap-4 md:gap-8">
        <div className="w-full flex justify-center">
          <Icon fontSize={192} icon="lets-icons:user-box-light" />
        </div>
        <div className="w-full h-full flex flex-col justify-between p-4 md:p-8">
          <div className="w-full flex flex-col gap-2">
          {/* <h2 className="text-xl md:text-2xl lg:text-3xl font-semibold">
            Personal Info
          </h2> */}
          <ul className="w-full flex flex-col gap-1">
            <li className="text-lg md:text-xl font-medium">
              First Name:{" "}
              <span className="font-normal">{profileData.first_name}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Last Name:{" "}
              <span className="font-normal">{profileData.last_name}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Email: <span className="font-normal">{profileData.email}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              City:{" "}
              <span className="font-normal">{profileData.city}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Institution:{" "}
              <span className="font-normal">{profileData.institution}</span>
            </li>
            <li className="text-lg md:text-xl font-medium">
              Subjects:{" "}
              <span className="font-normal">{subjectsList.length > 0 ? subjectsList.map((sub: any) => sub.name).join(", ") : "You dont have any subjects" }</span>
            </li>
          </ul>
          </div>
          <button onClick={() => openModal(profileData)} className="w-16 self-end flex items-center gap-1 py-1 px-2 mt-4 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white capitalize">
            <Icon icon="mage:edit" /> Edit
          </button>
        </div>
      </div>
    </div>
  );
};
