import React, {useState} from "react";
import Pagination from "react-js-pagination";

const Paging = () => {
  const [page, setPage] = useState(1);

  const handlePageChange = (page) => {
    setPage(page);
  };

  return (
    <Pagination 
    activePage={page}
    itemsCountPerPage={10}
    totalItemsCount={450}
    pageRangeDisplayed={}
    />
  );
}