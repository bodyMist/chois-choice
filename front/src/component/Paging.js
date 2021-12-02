import React, {useState} from "react";
import Pagination from "react-js-pagination";
import "./Paging.css"

export default function Paging({page, count, pageHandler}) {
  // const [page, setPage] = useState(1);



  return (
    <Pagination 
    activePage={page}
    itemsCountPerPage={10}
    totalItemsCount={count}
    pageRangeDisplayed={5}
    prevPageText={"<"}
    nextPageText={">"}
    onChange={pageHandler}
    />
  );
}