import { Icon } from "@iconify/react/dist/iconify.js";

interface institutionCardProps {
    index: number;
    openModal: (id: string) => void;
}

export const InstitutionsCard = ({ index, openModal }: institutionCardProps) => {
  return (
    <li
      className={`group relative w-full grid grid-cols-[1fr_6fr_2fr_2fr] p-2 ${
        index % 2 == 0 ? "bg-blue-100" : "bg-blue-50"
      } hover:bg-blue-700 rounded-md hover:text-white cursor-pointer`}
      onClick={() => openModal(`${index}`)}
    >
      <span className="group-hover:opacity-0">{index + 1}.</span>
      <span>College of Science and Technology</span>
      <span>MoonCity</span>
      <span>MoonState</span>
      <div className="hidden absolute top-0 left-0 h-full group-hover:flex items-center">
        <button className="w-8 h-8 flex items-center justify-center p-2 text-white hover:bg-white hover:text-black rounded">
          <Icon icon="material-symbols:delete-outline" />
        </button>
      </div>
    </li>
  );
};
