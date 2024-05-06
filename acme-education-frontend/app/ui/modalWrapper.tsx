// wraps a component and a modal

import React, { useState } from "react";
import { User } from "../types";

interface props {
  Component: React.ComponentType<{
    openModal: (val: any) => void;
  }>;
  Modal: React.ComponentType<{
    closeModal: () => void;
    item: any;
  }>;
  user?: User
}

interface profileProps {
  ProfileComponent: React.ComponentType<{
    user: User
    openModal: (val: any) => void;
  }>;
  Modal: React.ComponentType<{
    closeModal: () => void;
    item: any;
  }>;
  user: User
}


export const ModalWrapper = ({ Component, Modal, user }: props) => {
  const [isModal, setModal] = useState(false);
  const [selectedItem, setItem] = useState<any>();
  const openModal = (item: any) => {
    setModal(true);
    setItem(item);
  };
  const closeModal = () => setModal(false);
  return (
    <>
      <Component openModal={openModal} />
      {isModal && <Modal closeModal={closeModal} item={selectedItem} />}
    </>
  );
};

export const ProfileModalWrapper = ({ ProfileComponent, Modal, user }: profileProps) => {
  const [isModal, setModal] = useState(false);
  const [selectedItem, setItem] = useState<any>();
  const openModal = (item: any) => {
    setModal(true);
    setItem(item);
  };
  const closeModal = () => setModal(false);
  return (
    <>
      <ProfileComponent openModal={openModal} user={user} />
      {isModal && <Modal closeModal={closeModal} item={selectedItem} />}
    </>
  );
};
