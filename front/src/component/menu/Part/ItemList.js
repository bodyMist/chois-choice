import Item from "./Item";

export default function ItemList({list}) {
  return (
    <ul>
      {list.map((listData) => (
        <Item 
          key={listData.component_component.component_id}
          list={listData}
        />
      ))}
    </ul>

  );
}