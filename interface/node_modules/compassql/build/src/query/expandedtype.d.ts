import { Type } from 'vega-lite/build/src/type';
export declare namespace ExpandedType {
    const QUANTITATIVE: "quantitative";
    const ORDINAL: "ordinal";
    const TEMPORAL: "temporal";
    const NOMINAL: "nominal";
    const KEY: 'key';
}
export declare type ExpandedType = Type | typeof ExpandedType.KEY;
export declare function isDiscrete(fieldType: any): boolean;
