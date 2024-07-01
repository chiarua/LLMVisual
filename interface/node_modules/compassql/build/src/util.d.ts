import { isArray } from 'datalib/src/util';
import { Flag } from 'vega-lite/build/src/util';
export { cmp, keys, duplicate, extend, isObject, isBoolean, toMap } from 'datalib/src/util';
export { isArray };
export interface Dict<T> {
    [key: string]: T;
}
export declare function contains(array: any[], item: any): boolean;
export declare function every<T>(arr: T[], f: (item: T, key: number) => boolean): boolean;
export declare function forEach(obj: any, f: (item: any, key: number | string, i: number) => void, thisArg?: any): void;
export declare function some<T>(arr: T[], f: (item: T, key: number | string, i: number) => boolean): boolean;
export declare function nestedMap(array: any[], f: (item: any) => any): any[];
/** Returns the array without the elements in item */
export declare function without<T>(array: Array<T>, excludedItems: Array<T>): T[];
export declare function flagKeys<S extends string>(f: Flag<S>): S[];
export declare type Diff<T extends string, U extends string> = ({
    [P in T]: P;
} & {
    [P in U]: never;
} & {
    [x: string]: never;
})[T];
