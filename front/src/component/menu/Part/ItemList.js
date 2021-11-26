import Item from "./Item";

export default function ItemList({list}) {
  return (
    <ul>
      {list.map((listData) => (
        <Item 
          list={listData}
        />
      ))}
    </ul>
  );
}